from quora_api.api.serializer import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.settings import api_settings

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = api_settings.

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = api_settings.


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
