from django.db import models

from config.models import BaseModel, BaseModelWithSoftDelete
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
    bank = models.OneToOneField(Bank, on_delete=models.CASCADE, null=True, blank=True)
    staffs = models.ManyToManyField('Role',
                                    through='Staff',
                                    related_name='staffs')
    website = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name


STAFF_ROLES = (
    ('Owner', 'owner'),
    ('Developer', 'developer'),
    ('Moderator', 'moderator')
)


class Role(models.Model):
    from users.models import User
    role = models.CharField(max_length=20, choices=STAFF_ROLES, default='owner')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.user.name, self.role)


class Staff(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return '%s : %s' % (self.business.name, self.role)


class BusinessVerification(BaseModel):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    cac_cert = models.FileField(upload_to=file_upload_path.document_upload_path, default='', blank=True)
    tax_doc = models.FileField(upload_to=file_upload_path.document_upload_path, default='', blank=True)
    personal_id = models.FileField(upload_to=file_upload_path.document_upload_path, default='', blank=True)
