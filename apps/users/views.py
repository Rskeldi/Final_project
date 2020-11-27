import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from .serializer import UserDetailSerializer, PasswordResetSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserActivationView(APIView):
    def get(self, request, *args, **kwargs):
        print('hello')
        uidb64 = kwargs.get('uidb64', None)
        token = kwargs.get('token', None)
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/api/v1/account/users/activation/"
        post_data = {'uid': uidb64, 'token': token}
        result = requests.post(post_url, data=post_data)
        return Response(result)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    def get_queryset(self):
        print(self.request.user.password)
        return super().get_queryset()


class UserPasswordReset(APIView):
    def get(self, request, *args, **kwargs):
        print('hello')
        uidb64 = kwargs.get('uidb64', None)
        token = kwargs.get('token', None)
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/api/v1/account/users/reset_password_confirm/"
        post_data = {'uid': uidb64, 'token': token}
        result = requests.post(post_url, data=post_data)
        return Response(result)


