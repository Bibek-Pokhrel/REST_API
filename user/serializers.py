from rest_framework import serializers
from django.contrib.auth.models import User


class Userserializers(serializers.Serializer):
    username=serializers.CharField()
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    email=serializers.CharField()
    password=serializers.CharField(write_only=True)
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)