from rest_framework import serializers
from .models import StudentDetails
from django.contrib.auth.models import User
import datetime
import json



class Testserializer(serializers.Serializer):
    email=serializers.CharField(max_length=200)
    address=serializers.CharField(max_length=200)
    phone_number=serializers.CharField(max_length=10)
    created_by=serializers.ReadOnlyField()
    created_at=serializers.ReadOnlyField()
    
    def create(self, validated_data):
        return StudentDetails.objects.create(created_by=User.objects.first()
                                             ,created_at=datetime.datetime.now(),**validated_data)
    