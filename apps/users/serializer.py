from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class PasswordResetSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, style={
        'input_type': 'password'}
                                     )
    password_confirmation = serializers.CharField(min_length=8, style={
        'input_type': 'password'}
                                                  )

    class Meta:
        model = User
        fields = ('password', 'password_confirmation')
