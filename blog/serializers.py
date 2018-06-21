from rest_framework import serializers
from . import models

class PostSerializers(serializers.ModelSerializer):

    class Meta:
    	model = models.Post
        depth = 1
    	fields = ('title', 'pk', 'created_date', 'published_date', 'likes', 'favourite', 'tags', 'published')

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ('id', 'post', 'detail', 'approve_comment')
