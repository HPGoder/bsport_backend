
from .test_setup import TestSetUp
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User
from bookings.views import UserViewset, BookingsViewset
from bookings.models import Bookings

class TestUserViews(TestSetUp):

    def test_public_user_can_read(self):
        #Let's create an user and a booking to test if an user with admin credidential can read the viewset
        user = User.objects.create(username='testuser', password='userpassword')
        Bookings.objects.create(name='test booking', date ='2021-01-21T14:53:00Z', description='test boooking', user=user)
        factory = APIRequestFactory()
        view = BookingsViewset.as_view({'get': 'list'})
        request = factory.get('/viewset/bookings/')
        response=view(request)
        response.render()
        self.assertEqual(response.status_code, 200)

    def test_public_user_cannot_post(self):
        #Here we just try to post a new booking without any user credidentail
        factory = APIRequestFactory()
        view = BookingsViewset.as_view({'get': 'list'})
        request = factory.post('/viewset/bookings/', self.new_booking, format='json')
        response=view(request)
        response.render()
        self.assertEqual(response.status_code, 401)

    def test_admin_user_can_post(self):
        factory = APIRequestFactory()
        view = BookingsViewset.as_view({'post': 'create'})
        request = factory.post('/viewset/bookings/', self.new_booking, format='json')
        request.user = self.user
        force_authenticate(request, user=self.user)
        response=view(request)
        response.render()
        self.assertEqual(response.status_code, 201)


    def test_admin_user_can_update(self):
        factory = APIRequestFactory()
        view = BookingsViewset.as_view({'get' : 'list', 'put' : 'update', 'post': 'create'})
        #let's create a booking and then update it
        Bookings.objects.create(name='test booking 2', date ='2021-01-21T14:53:00Z', description='test boooking', user=self.user)
        factory=APIRequestFactory()
        request = factory.put('/viewset/bookings/', self.updated_booking, format='json')
        request.user = self.user
        force_authenticate(request, user=self.user)
        response=view(request, pk=2)
        response.render()
        self.assertEqual(response.status_code, 200)