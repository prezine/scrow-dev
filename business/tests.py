from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.utils import timezone

from business.models import Business
from users.models import User


class TestBankVerification(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('business:bank_details')
        data = {
            'name': 'Samuel',
            'email': 'sam@gmail.com',
            'phone': '0903218393',
            'password': 123456,
            'calling_code': 234,
            'country': 'Nigeria',
            'state': 'Rivers State',
            'city': 'PH',
            'address': '32 bori street',
            'gender': 'Male',
            'date_of_birth': timezone.now().date()
        }

        self.user = User.objects.create(**data)
        self.business_data = {
            'name': 'ON and Off',
            'email': 'confidence@gmail.com',
            'country': 'Nigeria',
            'state': 'Rivers State',
            'city': 'PH',
            'address': '32 bori street',
            'category': 'One',
            'sub_category': 'Two',
            'userId': self.user.pk,
            'business_type': 'Running'
        }

    def test_bank_verification(self):
        self.client.force_login(self.user)
        data = {
            'bank_name': 'GTBank',
            'account_number': 339393839,
            'account_name': 'Small Man',
            'bvn': '37393003949403030'
        }
        business_response = self.client.post(reverse('business:create'), self.business_data)
        self.assertEquals(business_response.status_code, 201)
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bank details updated!')
