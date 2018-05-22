# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re

from django.utils import timezone
from django.shortcuts import render, reverse, get_object_or_404
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

def get_redirected(queryset_or_class, lookups, validators):
    """
    Calls get_object_or_404 and conditionally builds redirect URL
    """
    obj = get_object_or_404(queryset_or_class, **lookups)
    for key, value in validators.items():
        if value != getattr(obj, key):
            return obj, obj.get_absolute_url()
    return obj, None


def post_details(request, slug, post_pk):
    #post = models.Post.objects.get(pk=post_pk)
    post, post_url = get_redirected(models.Post, {'pk':post_pk}, {'slug': slug })
    #return render(request, 'blog/post_details.html', {'post': post })
    if post_url:
        return HttpResponseRedirect(post_url)
    else:
        return render(request, 'blog/post_details.html', {'post': post})

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
            post, post_url = get_redirected(models.Post, {'pk':post.pk}, {'slug': post.slug })
            if post_url:
                return HttpResponseRedirect(post_url)
            else:
                return render(request, 'blog/post_details.html', {'post': post })
            #return HttpResponseRedirect(
            #    reverse(
            #        'post_details',
            #            args=(post.pk,)
            #            )
            #    )
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

def like_post(request):
    #This function updates a part of HTML
    post_id = None
    if request.method == 'GET':
        post_id = request.GET['post_id']

    likes = 0

    if post_id:
        post = models.Post.objects.get(id=int(post_id))
        if post:
            likes = post.likes + 1
            post.likes = likes
            post.save()

    return HttpResponse("<p>No of Likes : %s </p>" % likes)

def post_comment(request, post_pk):
    """
    This function to be used if you want to post comment and then rel-
    -oad page immediately and show the new comment
    """
    post = get_object_or_404(models.Post, pk=post_pk)
    form = forms.CommentForm()
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    else:
        form = forms.CommentForm()

    return HttpResponseRedirect(post.get_absolute_url())

def post_comment_on_fly(request):
    """
    This function is to be used, if you want to create
    comment using an ajax using jquery call and s
    show the comment immediately after used submits the comment.
    """
    if request.method == 'GET':
        post_pk =  request.GET['post_pk']
        comment_details = request.GET['comment_details']
        post = get_object_or_404(models.Post, pk=post_pk)
        comment = models.Comment.objects.create(post=post, detail=comment_details)
        date_time = comment.created_date.strftime("%B %d, %Y %H:%M %p")
        body = """
            <div class="comment">
                <div class="date">
                    %s
                </div>
                <p>%s : by <strong>%s</strong></p>
            """ % (date_time, comment.detail, comment.post.author)
    return HttpResponse(body)

def home(request):
    tags = get_all_tags()
    fav_posts = get_favourites()
    latest_post, latest_post_image = get_latest_post()
    for post in fav_posts:
        first_image = get_images_from_post_description(post.pk)
        if first_image:
            post.first_image = first_image
        else:
            post.first_image = '#'
    return render(request, 'blog/home_page.html',
     {
     'fav_posts':fav_posts,
     'latest_post': latest_post,
     'latest_post_image':latest_post_image,
     'tags':tags,
     })

def all_posts_for_tag(request, tag):
    posts = get_post_for_tag(tag)
    return render(request, 'blog/post_list.html', {'posts':posts})

def get_all_tags():
    return models.Tag.objects.all()

def get_post_for_tag(tagname):
    posts = models.Post.objects.filter(tags__name=tagname)
    return posts


def get_favourites():
    #This function returns a list of post with fav as True
    return models.Post.objects.filter(published=True, favourite=True)

def get_latest_post():
    latest = models.Post.objects.latest('created_date')
    image = get_images_from_post_description(latest.pk)
    return latest, image

def get_images_from_post_description(post_pk):
    post = models.Post.objects.get(pk=post_pk)
    des = post.text
    #first_image = re.findall('(?<=src=")https.*jpg', des)
    images = re.findall('(?<=src=").*jpg', des)
    images =  sorted(images)
    if images:
        return images[0]
    return False

def error_404(request):
    data = {}
    return render(request, 'blog/error_404.html')

def error_500(request):
    data = {}
    return render(request, 'blog/error_500.html')

def about_me(request):
    return render(request, 'blog/about_me.html')
