from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
import vichars.serializers as helpers
import vichars.models as model 
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
# Create your views here.

    
class vicharAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = helpers.postSerializers
    lookup_url_kwarg = 'pk'
    queryset = model.vichars.objects.all()


class vicharCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = helpers.postSerializers
    queryset = model.vichars.objects.all()

    def post(self, request,format = None):
        request.data.update({'user':request.user.userId})
        
        post = helpers.postSerializers(data = request.data)
        print(post.initial_data)
        if post.is_valid(raise_exception=True):
            post.save()
            return Response(post.data,status = status.HTTP_201_CREATED)
        return Response(post.errors, status = status.HTTP_400_BAD_REQUEST)    

class commentAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = helpers.commentSerializers
    lookup_url_kwarg = 'pk'
    queryset = model.comment.objects.all()

class commentCreateAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request,pk,format = None):
        request.data.update({'user':request.user.userId})
        request.data.update({'vicharId':pk})
        comment = helpers.commentCreateSerializers(data = request.data)
        if comment.is_valid(raise_exception=True):
            comment.save()
            return Response(comment.data,status = status.HTTP_201_CREATED)
        return Response(comment.errors, status = status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def likePost(request,pk,format = None):
    vicharId = pk
    vichar = get_object_or_404(model.vichars.objects.all(),vicharId = vicharId)
    vichar.likes += 1
    vichar.user.points+=1
    vichar.user.save()
    vichar.save()
    return Response("message :Liked", status=status.HTTP_200_OK)
  
        

    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def removeLike(request,pk,format = None):
    vicharId = pk
    vichar = get_object_or_404(model.vichars.objects.all(),vicharId = vicharId)
    vichar.likes -= 1
    vichar.user.points-=1
    vichar.user.save()
    vichar.save()
    return Response("message : Removed Liked", status=status.HTTP_200_OK)
        