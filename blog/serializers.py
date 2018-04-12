from rest_framework import serializers
from . import models

class CommentSerializers(serializers.ModelSerializers):
	class Meta:
		model = model.Comment