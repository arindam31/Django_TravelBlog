"""Module for APIs"""

from django.shortcuts import get_object_or_404
from rest_framework import viewsets  # For routers
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response

from blog import models, serializers


class PostCreateApi(generics.ListCreateAPIView):
    """API for creating Post"""
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializers


class RetrieveUpdateDestroyPost(generics.RetrieveUpdateDestroyAPIView):
    """API for Retrieve, update or destroy Post"""
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializers


class ListCreateComment(generics.ListCreateAPIView):
    """API for creating comments"""
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializers

    def get_queryset(self):
        """Get queryset"""
        return self.queryset.filter(post_id=self.kwargs.get('post_pk'))

    def perform_create(self, serializer):
        """
        This is the method which is run, right when object is being created by the view.
        """
        post = get_object_or_404(models.Post, pk=self.kwargs.get('post_pk'))
        serializer.save(post=post)


class RetrieveUpdateDestroyComment(generics.RetrieveUpdateDestroyAPIView):
    """ API view for Comment """
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
    """ View set for Post """
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializers

    @action(detail=True, methods=['get'])  # Hence /post/comments
    def comments(self):
        """Get comments"""
        post = self.get_object()  # Internal function to get object
        serializer = serializers.CommentSerializers(post.comments.all(), many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    """ View set for Comment """
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializers
