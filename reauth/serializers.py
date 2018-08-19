from rest_framework import serializers, fields, validators
from .models import User
from collections import OrderedDict

# USER
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('pk', 'email', 'fio', 'phone', 'avatar', 'date_joined',)

class AuthSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('pk', 'email', 'fio', 'phone', 'password', 'avatar', 'date_joined',)
