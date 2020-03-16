from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)

from config.models import BaseModelWithSoftDelete
from utils.files import file_upload_path


class UserManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        user = self.model(email=email, **extra_fields)
        user.set_password(password.lower())
        user.save(using=self._db)
        return user


GENDER_CHOICES = (
    ('Male', 'male'),
    ('Female', 'female'),
)


class User(AbstractBaseUser, PermissionsMixin, BaseModelWithSoftDelete):
    from business.models import Business

    name = models.CharField(max_length=300, db_index=True, unique=True)
    email = models.EmailField(max_length=300, db_index=True, unique=True)
    phone = models.CharField(max_length=20, db_index=True, unique=True)
    calling_code = models.IntegerField(default=234)
    photo = models.ImageField(upload_to=file_upload_path.profile_image_upload_path,
                              default='profile-photo-fallback.png', blank=True)
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)
    active_business = models.ForeignKey(Business, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_activated = models.DateTimeField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone', 'calling_code']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

    def __str__(self):
        return self.name
