from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Bookings
from .serializers import UserSerializer, BookingsSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.decorators import action

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadOnly]



    
class BookingsViewset(viewsets.ModelViewSet):
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer
    permission_classes = [IsAdminOrReadOnly]

