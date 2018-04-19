from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^posts/$', views.post_list, name='post_list'),
	url(r'^post/about_me/$', views.about_me, name='about_me'),
	url(r'^(?P<post_pk>\d+)/$', views.post_details, name='post_details'), 
	url(r'^post/create/$', views.create_post, name='post_create'),
	url(r'^post/edit/(?P<post_pk>\d+)$', views.edit_post, name='post_edit'),
	url(r'^search/post/$', views.search_post, name='post_search'),
	url(r'^post/like/$', views.like_post, name='like_post'),

]

if settings.DEBUG:
	urlpatterns += [
		url('^error/404/$', views.error_404, name='404page'), 	
		url('^error/500/$', views.error_500, name='500page'), 	
					]

