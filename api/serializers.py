from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, required=False)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    is_staff = serializers.BooleanField()
    is_active = serializers.BooleanField()
    cpf = serializers.CharField()
    address = serializers.JSONField()
    phone1 = serializers.CharField()
    phone2 = serializers.CharField()
    phone_other1 = serializers.CharField()
    phone_other2 = serializers.CharField()
    whats = serializers.CharField()
    date_nasc = serializers.DateField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass