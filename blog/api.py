from django.shortcuts import get_object_or_404
from rest_framework import viewsets  # For routers
from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from blog import models, serializers


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
        # get_queryset returns  multiple objects
        return self.queryset.filter(post_id=self.kwargs.get('post_pk'))

    def perform_create(self):
        """
        This is the method which is run, right when object is being created by the view.
        """
        post = get_object_or_404(models.Post, pk=self.kwargs.get('post_pk'))
        serializer.save(post=post)


class RetriveUpdateDestroyComment(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializers

    def get_object(self):
        # Returns a single object
        return get_object_or_404(
                self.get_queryset(),
                post=self.kwargs.get('post_pk'),
                pk=self.kwargs.get('pk')
                )


# Routers are REST Frameworks way of automating URL creation for API views
class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializers

    @action(detail=True, methods=['get'])  # Hence /post/comments
    def comments(self, request, pk=None):
        post = self.get_object() # Internal function to get object
        serializer = serializers.CommentSerializers(
            post.comments.all(), many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializers
