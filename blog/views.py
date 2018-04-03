# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render
from . import models

# Create your views here.
def post_list(request):
	posts =models.Post.objects.filter(created_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})


def post_details(request, post_pk):
	post = models.Post.objects.get(pk=post_pk)
	return render(request, 'blog/post_details.html', {'post': post })

	
