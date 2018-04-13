from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from . import models

class ListPostApi(APIView):
    def get(self, request, format=None):
        posts = models.Post.objects.all()
        serializer = serializers.PostSerializers(posts, many=True) #If its a query list, many = True
        return Response(serializer.data)
