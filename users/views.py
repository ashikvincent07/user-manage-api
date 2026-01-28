from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import Users
from users.serializers import UsersSerializers


class UsersCreateListView(APIView):

    def post(self, request, *args, **kwargs):

        data = request.data

        serializer_instance = UsersSerializers(data=data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            Users.objects.create(**cleaned_data)

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        
    

    def get(self, request, *args, **kwargs):

        qs = Users.objects.all()

        serializer_instance = UsersSerializers(qs, many=True)

        return Response(data=serializer_instance.data)
