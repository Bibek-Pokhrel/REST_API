from rest_framework.decorators import APIView
from user.serializers import Userserializers
from django.http import JsonResponse
from rest_framework import status
from django.contrib.auth.models import User
from user import global_message as g



class UserRegisterApiView(APIView):
    def get(self,request):
        try:
            data=User.objects.all()
            serializers=Userserializers(data,many=True)
            return JsonResponse({g.RESPONSE_KEY:serializers.data},status=200)
        except Exception as exe:
            print(exe)
            return JsonResponse({g.RESPONSE_KEY:g.SERVER_ERROR},status=500)
    def post(self,request):
        try:
            serializers=Userserializers(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return JsonResponse({g.RESPONSE_KEY:g.CREATE_KEY},status=200)
            return JsonResponse({g.RESPONSE_KEY:serializers.errors},status=400)
        except Exception as exe:
            print(exe)
            return JsonResponse({g.RESPONSE_KEY:g.SERVER_ERROR},status=500)
        