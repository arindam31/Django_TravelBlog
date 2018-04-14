from django.conf.urls import url
from . import views
from . import api

urlpatterns = [
        url(r'^$', api.PostCreateApi.as_view(), name='api_post_list'),
        url(r'^postedit/(?P<pk>\d+)/$', api.RetriveUpdateDestropPost.as_view(), 
            name='api_post_update')
        ]
