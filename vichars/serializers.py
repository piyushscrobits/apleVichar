from users.serializers import userSerializer
from rest_framework import serializers
from vichars.models import vichars,comment

class commentSerializers(serializers.ModelSerializer):
    user = userSerializer(read_only = True)
    class Meta:
        model = comment
        fields = '__all__'

class commentCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = ['comment','user','vicharId','commentId']
        read_only_fields = ['commentId']

class postSerializers(serializers.ModelSerializer):
    #user = userSerializer()
    postComment = commentSerializers(many = True,read_only = True)
    class Meta:
        model = vichars
        fields = ['vicharId','user','createdAt','likes','vichar','postComment']
        read_only_fields = ['vicharId','likes','createdAt','postComment']



