from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase


class TestUserRegistration(APITestCase):
    def setUp(self):
        self.url = reverse('users:user_registration')

    def test_user_registration(self):
        data = {
            'name': 'Samuel',
            'email': 'sam@gmail.com',
            'phone': '0903218393',
            'password': 123456,
            'retype_password': 123456,
            'calling_code': 234,
            'country': 'Nigeria',
            'state': 'Rivers State',
            'city': 'PH',
            'address': '32 bori street',
            'gender': 'Male',
            'date_of_birth': timezone.now().date()
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
