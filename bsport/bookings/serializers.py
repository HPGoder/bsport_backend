from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Bookings



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'email', 'date_joined']

class BookingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookings
        fields = '__all__'