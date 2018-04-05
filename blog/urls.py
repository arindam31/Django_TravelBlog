from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'(?P<post_pk>\d+)/$', views.post_details, name='post_details'), 
	url(r'^post/create/$', views.create_post, name='post_create'),
	url(r'^post/edit/(?P<post_pk>\d+)$', views.edit_post, name='post_edit'),
	url(r'^search/post/$', views.search_post, name='post_search'),
]

