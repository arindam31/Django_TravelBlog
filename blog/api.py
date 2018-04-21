from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from . import models

class ListPostApi(APIView):
    #This class is not used ..we use the below class now
    def get(self, request, format=None):
        posts = models.Post.objects.all()
        serializer = serializers.PostSerializers(posts, many=True) #If its a query list, many = True
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.PostSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PostCreateApi(generics.ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializers


class RetriveUpdateDestroyPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializers

class ListCreateComment(generics.ListCreateAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializers

    def get_queryset(self):
        return self.queryset.filter(post_id=self.kwargs.get('post_pk'))

class RetriveUpdateDestroyComment(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializers


