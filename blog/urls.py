from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^posts/$', views.post_list, name='post_list'),
	url(r'^post/comment/$', views.post_comment_on_fly, name='comment_create'),
	url(r'^post/(?P<post_pk>\d+)/edit/$', views.edit_post, name='post_edit'),
	url(r'^post/about_me/$', views.about_me, name='about_me'),
	url(r'^post/(?P<post_pk>\d+)/(?P<slug>[-\w\d]+)/$', views.post_details, name='post_details'),
	url(r'^post/create/$', views.create_post, name='post_create'),
	url(r'^post/like/$', views.like_post, name='like_post'),
	url(r'^search/post/$', views.search_post, name='post_search'),
	url(r'^posts/tag/(?P<tag>[\w]+)/$', views.all_posts_for_tag, name='tag_posts'),

	# City related urls
	url(r'^post/city/(?P<city_name>\w+)/(?P<city_post_pk>\d+)/(?P<slug>[-\w\d]+)/$', views.city_post, name='city_details'),
]

if settings.DEBUG:
	urlpatterns += [
		url('^error/404/$', views.error_404, name='404page'),
		url('^error/500/$', views.error_500, name='500page'),
					]

