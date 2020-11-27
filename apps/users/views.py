import requests
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import PasswordResetSerializer

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


class UserPasswordReset(APIView):
    serializer_class = PasswordResetSerializer

    def post(self, request, **kwargs):
        uid = kwargs.get('uidb64')
        token = kwargs.get('token')
        password = self.request.data.get('password')
        password_confirmation = self.request.data.get('password_confirmation')
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/api/v1/account/users/reset_password_confirm/"
        post_data = {'uid': uid, 'token': token, 'new_password': password,
                     're_new_password': password_confirmation}
        result = requests.post(post_url, data=post_data)
        return Response(result)
