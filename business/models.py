from django.db import models
from django.utils import timezone

from config.models import BaseModel, BaseModelWithSoftDelete
from finance.models import Bank
from utils.files import file_upload_path

BUSINESS_TYPE = (
    ('Running', 'running'),
    ('Startup', 'startup')
)

CURRENCY = (
    ('NGN', 'NGN'),
    ('USD', 'USD')
)


class Business(BaseModelWithSoftDelete):
    name = models.CharField(max_length=300, db_index=True, unique=True)
    email = models.EmailField(max_length=200, unique=True, db_index=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    photo = models.ImageField(upload_to=file_upload_path.business_avatar_upload_path,
                              default='business-photo-fallback.png', blank=True)
    business_type = models.CharField(max_length=20, choices=BUSINESS_TYPE, default='startup')
    is_active = models.DateTimeField(null=True, blank=True)
    request_verification = models.DateTimeField(null=True, blank=True)
    bank = models.OneToOneField(Bank, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=20, default='')
    website = models.CharField(max_length=300, default='', null=True, blank=True)
    currency = models.CharField(max_length=10, choices=CURRENCY, default='NGN')
    description = models.TextField(null=True, blank=True)
    support_email = models.EmailField(max_length=300, default='', null=False, blank=True)
    chargeback_email = models.EmailField(max_length=300, default='', null=False, blank=True)
    twitter_username = models.CharField(max_length=100, default='', null=False, blank=True)
    instagram_username = models.CharField(max_length=100, default='', null=False, blank=True)
    facebook_username = models.CharField(max_length=100, default='', null=False, blank=True)
    linkedin_username = models.CharField(max_length=100, default='', null=False, blank=True)

    def __str__(self):
        return self.name

    def request_account_verification(self):
        self.request_verification = timezone.now()
        # Todo: Send request to admin to verify business details
        self.save()


STAFF_ROLES = (
    ('Owner', 'owner'),
    ('Developer', 'developer'),
    ('Moderator', 'moderator')
)

DOCUMENT_TYPE = (
    ('RC Document', 'rc'),
    ('BN Document', 'bn'),
    ('NEPZA Document', 'nepza'),
    ('CAC IT Document', 'cac')
)


class TeamMember(models.Model):
    from users.models import User
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=STAFF_ROLES, default='owner')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s : %s' % (self.business.name, self.role)


class BusinessVerification(BaseModel):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    document = models.FileField(upload_to=file_upload_path.document_upload_path, default='', blank=True)
    document_type = models.CharField(choices=DOCUMENT_TYPE, max_length=100)
    bvn = models.CharField(default='', max_length=100)
    date_company_started = models.DateField(blank=True, null=True)


class StaffInvite(BaseModel):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    invite_id = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    role = models.CharField(max_length=20)
    is_active = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.invite_id
