from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User


class PasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=8)
    password_confirmation = serializers.CharField(min_length=8)


    # def validate(self, attrs):
    #     password = attrs.get('password')
    #     password_confirmation = attrs.pop('password_confirmation')
    #
    #     if password != password_confirmation:
    #         raise serializers.ValidationError("Passwords don't match")
    #     return attrs
