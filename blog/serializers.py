from rest_framework import serializers
from . import models

class CommentSerializers(serializers.ModelSerializer):
	class Meta:
		model = models.Comment
		fields = ('detail', 'post')