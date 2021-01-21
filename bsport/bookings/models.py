from django.db import models
from django.contrib.auth.models import User


class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    booking_date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=500)

