# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login
from django.db.models import Q
from . import models
from . import forms


# Create your views here.
def post_list(request):
    if not request.user.is_staff or not request.user.is_superuser:
        posts = models.Post.objects.filter(published=True, created_date__lte=timezone.now()).order_by('published_date')
    else:
        posts = models.Post.objects.filter(created_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_details(request, post_pk):
    post = models.Post.objects.get(pk=post_pk)
    return render(request, 'blog/post_details.html', {'post': post })

def create_post(request):
    #This will help us control who has permission to create posts
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = forms.BlogPostForm()
    if request.method == 'POST':
        form = forms.BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # Below redirection is also an example of how I can redirect to the post I just created.
            return HttpResponseRedirect(post.get_absolute_url())
    return render(request, 'blog/post_create.html', {'form':form})

def edit_post(request, post_pk):
    #This will help us control who has permission to create posts
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    post = models.Post.objects.get(pk=post_pk)
    form = forms.BlogPostForm(instance=post)

    if request.method == 'POST':
        form = forms.BlogPostForm(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(post.get_absolute_url())
    return render(request, 'blog/post_create.html', {'form':form})

def search_post(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        if not keyword:
            raise Http404
        else:
            posts = models.Post.objects.filter(
            Q(title__icontains=keyword) | Q(text__icontains=keyword), 
            created_date__lte=timezone.now(), 
            ).order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts':posts})    







