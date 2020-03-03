from django.db import models

from config.models import BaseModel
from finance.models import Bank
from utils.files import file_upload_path


BUSINESS_TYPE = (
    ('Running', 'running'),
    ('Startup', 'startup')
)


class Business(BaseModel):
    name = models.CharField(max_length=300, db_index=True, unique=True)
    email = models.EmailField(max_length=200, unique=True, db_index=True)
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    photo = models.ImageField(upload_to=file_upload_path.business_avatar_upload_path, default='', blank=True)
    category = models.CharField(max_length=200)
    sub_category = models.CharField(max_length=200)
    business_type = models.CharField(max_length=20, choices=BUSINESS_TYPE, default='startup')
    is_active = models.DateTimeField(null=True, blank=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True, blank=True)
    staffs = models.ManyToManyField('StaffRole', related_name='staffs')

    def __str__(self):
        return self.name


STAFF_ROLES = (
    ('Owner', 'owner'),
    ('Developer', 'developer'),
    ('Moderator', 'moderator')
)


class StaffRole(BaseModel):
    from users.models import User
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    roles = models.CharField(max_length=20, choices=STAFF_ROLES, default='owner')
