from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import *


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, required=False)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    is_staff = serializers.BooleanField()
    is_active = serializers.BooleanField()
    cpf = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    phone1 = serializers.SerializerMethodField()
    phone2 = serializers.SerializerMethodField()
    phone_other1 = serializers.SerializerMethodField()
    phone_other2 = serializers.SerializerMethodField()
    whats = serializers.SerializerMethodField()
    date_nasc = serializers.SerializerMethodField()

    def get_cpf(self, instance):
        return ExtendUser.objects.get(user_id=instance.id).cpf

    def get_address(self, instance):
        return ExtendUser.objects.get(user_id=instance.id).address

    def get_phone1(self, instance):
        return ExtendUser.objects.get(user_id=instance.id).phone1

    def get_phone2(self, instance):
        return ExtendUser.objects.get(user_id=instance.id).phone2

    def get_phone_other1(self, instance):
        return ExtendUser.objects.get(user_id=instance.id).phone_other1

    def get_phone_other2(self, instance):
        return ExtendUser.objects.get(user_id=instance.id).phone_other2

    def get_whats(self, instance):
        return ExtendUser.objects.get(user_id=instance.id).whats

    def get_date_nasc(self, instance):
        return ExtendUser.objects.get(user_id=instance.id).date_nasc

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = LogModel
        fields = '__all__'


class BookRentalSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookRentalModel
        fields = '__all__'
