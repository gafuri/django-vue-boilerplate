from rest_framework import viewsets, status, generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer, AuthSerializer
from .forms import RegisterForm
import json

class UsersViewSet(viewsets.ModelViewSet) :
  queryset = User.objects.all()
  serializer_class = UserSerializer


class RegisterUsers(generics.CreateAPIView):
    serializer_class = AuthSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        password = request.data.get("password", "")
        email = request.data.get("email", "")

        f = RegisterForm(request.data)
        if(f.is_valid()) :
          new_user = User.objects.create_user(
            **f.cleaned_data
          )

          return Response(status=status.HTTP_201_CREATED)
        else :
          return Response(
              data = f.errors,
              status=status.HTTP_400_BAD_REQUEST
          )


        return Response(status=status.HTTP_201_CREATED)

# from django.core.mail import send_mail
# send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)
