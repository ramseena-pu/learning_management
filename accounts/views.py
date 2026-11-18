from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from accounts.serializers import Userserializer

# Create your views here.
class UserCreateView(CreateAPIView):
    serializer_class=Userserializer
    