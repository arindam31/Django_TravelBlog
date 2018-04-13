from django.conf.urls import url
from . import views
from . import api

urlpatterns = [
        url(r'^$', api.ListPostApi.as_view(), name='api_course_list'),
        ]
