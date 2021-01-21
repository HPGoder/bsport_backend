from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TestSetUp(APITestCase):


    def setUp(self):
        self.new_booking={
            'name': 'test booking',
            'date' : '2021-01-21T14:53:00Z',
            'booking_date' : '2021-01-20T13:54:00.889404Z',
            'description' : 'test boooking',
            'user' : '1',
        }
        return super().setUp()



    def tearDown(self):
        return super().tearDown()