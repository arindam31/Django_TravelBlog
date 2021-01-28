from django.conf.urls import url

from . import api, views

urlpatterns = [
        url(r'^$', api.PostCreateApi.as_view(), name='api_post_list'),
        url(r'^postedit/(?P<pk>\d+)/$', api.RetriveUpdateDestroyPost.as_view(),
            name='api_post_update'),
        url(r'^(?P<post_pk>\d+)/comments/$', api.ListCreateComment.as_view(), name='api_comment_list'),
        url(r'^(?P<post_pk>\d+)/comment/(?P<pk>\d+)/$', api.RetriveUpdateDestroyComment.as_view(), name='api_comment_edit'),
        ]
