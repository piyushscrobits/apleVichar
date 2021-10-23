from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from users.serializers import  userSerializer
import users.serializers as helpers
from users.models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework import generics
from django.shortcuts import get_object_or_404

# Create your views here.
class userAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'
    serializer_class = userSerializer
    queryset = CustomUser.objects.all()

class usersList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = userSerializer

    def post(self, request,format = None):
        user = userSerializer(data = request.data)   #serialize data given by user
        if user.is_valid(raise_exception=True):
            user.save()
            current_user = CustomUser.objects.get(username=request.data['username'])
            current_user.set_password(request.data['password'])
            current_user.save()
            user = userSerializer(current_user)
            return Response(user.data,status = status.HTTP_201_CREATED)
        return Response(user.errors, status = status.HTTP_400_BAD_REQUEST)