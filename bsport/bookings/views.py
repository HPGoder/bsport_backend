from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Bookings
from .serializers import UserSerializer, BookingsSerializer
from .permissions import IsAdminOrReadOnly

class UserViewset(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadOnly]


class BookingsViewset(viewsets.ModelViewSet):
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer
    permission_classes = [IsAdminOrReadOnly]