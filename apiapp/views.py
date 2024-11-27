from django.shortcuts import render
from apiapp.serializers import UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["POST"])
def register_user(request):
    serializer =UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED)  # Returning a 201 CREATED status on successful creation
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 