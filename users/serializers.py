from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from users.models import CustomUser

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','password','userId','gender','totalVichars','points','is_active','first_name','last_name')
        read_only_fields = ['is_active','userId','totalVichars','points']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 4,'required': False},'username': {'required': True}}