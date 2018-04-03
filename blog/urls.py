from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
]

