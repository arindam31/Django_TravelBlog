"""
Module for serializers
"""

from rest_framework import serializers

from blog import models


class PostSerializers(serializers.ModelSerializer):
    """
    Serializer for Post.
    """

    class Meta:
        """Meta Class"""
        model = models.Post
        depth = 1  # This helps see full details of tags
        fields = (
            'title', 'pk', 'created_date', 'published_date',
            'likes', 'favourite', 'tags', 'published')

class CommentSerializers(serializers.ModelSerializer):
    """
    Serializer for Comment.
    """
    class Meta:
        """Meta Class"""
        model = models.Comment
        fields = ('id', 'post', 'detail')
