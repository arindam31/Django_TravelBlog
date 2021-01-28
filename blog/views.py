# -*- coding: utf-8 -*-
"""
Module for blog views.
"""
from __future__ import unicode_literals

import re

from django.db.models import Q
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog import forms, models


def post_list(request):
    """
    Function to get all posts for user
    """
    if not request.user.is_staff or not request.user.is_superuser:
        posts = models.Post.objects.filter(
            published=True, created_date__lte=timezone.now()).order_by('published_date')
    else:
        posts = models.Post.objects.filter(
            created_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


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
    """
    Function to get post details.
    """
    post, post_url = get_redirected(models.Post, {'pk': post_pk}, {'slug': slug})
    # return render(request, 'blog/post_details.html', {'post': post })
    if post_url:
        return HttpResponseRedirect(post_url)

    return render(request, 'blog/post_details.html', {'post': post})


def create_post(request):
    """
    Function to create a post.
    """
    # This will help us control who has permission to create posts
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = forms.BlogPostForm()
    if request.method == 'POST':
        form = forms.BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            post, post_url = get_redirected(models.Post, {'pk': post.pk}, {'slug': post.slug})
            if post_url:
                return HttpResponseRedirect(post_url)

            return render(request, 'blog/post_details.html', {'post': post})
    return render(request, 'blog/post_create.html', {'form': form})


def edit_post(request, post_pk):
    """
    Function to edit a post.
    """
    # This will help us control who has permission to create posts
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    post = models.Post.objects.get(pk=post_pk)
    form = forms.BlogPostForm(instance=post)

    if request.method == 'POST':
        form = forms.BlogPostForm(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(post.get_absolute_url())
    return render(request, 'blog/post_create.html', {'form': form})


def search_post(request):
    """
    Function to search a post.
    """
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        if not keyword:
            raise Http404

        posts = models.Post.objects.filter(
            Q(title__icontains=keyword) | Q(text__icontains=keyword),
            created_date__lte=timezone.now(),
        ).order_by('published_date')

        if posts:
            return render(request, 'blog/post_list.html', {'posts': posts})

        all_posts = models.Post.objects.filter(published=True).order_by('-created_date')
        return render(request, 'blog/post_list.html', {'all_posts': all_posts})


def like_post(request):
    """
    Function for like on a post.
    """
    # This function updates a part of HTML
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

    return HttpResponse("<div>%s</div>" % likes)


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

    return HttpResponseRedirect(post.get_absolute_url())


def post_comment_on_fly(request):
    """
    This function is to be used, if you want to create
    comment using an ajax using jquery call and s
    show the comment immediately after used submits the comment.
    """
    if request.method == 'GET':
        post_pk = request.GET['post_pk']
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
    """
    This is the view for launch page.

    We show here a mix of all kinds of things, like
    posts , latest , favourites , tags and city posts.
    """
    tags = get_all_tags()
    fav_posts = get_favourites()
    latest_post, latest_post_image = get_latest_post()
    all_posts = models.Post.objects.filter(published=True).order_by('-created_date')
    for post in fav_posts:
        first_image = get_images_from_post_description(post.pk)
        if first_image:
            post.first_image = first_image
        else:
            post.first_image = '#'  # Hash means...no link supplied..so no effect

    for post in all_posts:
        first_image = get_images_from_post_description(post.pk)
        if first_image:
            post.first_image = first_image
        else:
            post.first_image = '#'

    cities = models.CityPost.objects.filter(published=True)

    return render(request, 'blog/home_page.html',
                  {
                      'fav_posts': fav_posts,
                      'latest_post': latest_post,
                      'latest_post_image': latest_post_image,
                      'tags': tags,
                      'all_posts': all_posts,
                      'cities': cities,
                  })


def all_posts_for_tag(request, tag):
    """Get all posts with tag

    :param str tag: Tag
    """
    posts = get_post_for_tag(tag)
    return render(request, 'blog/post_list.html', {'posts': posts})


def get_all_tags():
    """Get all tags"""
    return models.Tag.objects.all()


def get_post_for_tag(tag_name):
    """Get all posts with tag"""
    posts = models.Post.objects.filter(tags__name=tag_name)
    return posts


def get_favourites():
    """This function returns a list of post with fav as True"""
    return models.Post.objects.filter(published=True, favourite=True)


def get_latest_post():
    """Get the last post as per creation date"""
    latest = models.Post.objects.latest('created_date')
    image = get_images_from_post_description(latest.pk)
    return latest, image


def get_images_from_post_description(post_pk):
    """Get images from post's description"""
    post = models.Post.objects.get(pk=post_pk)
    des = post.text
    # first_image = re.findall('(?<=src=")https.*jpg', des)
    images = re.findall('(?<=src=").*jpg', des)
    images = sorted(images)
    if images:
        return images[0]
    return False

def about_me(request):
    """
    This is a static wiki page for the Author
    """
    return render(request, 'blog/about_me.html')


def city_post(request, slug, city_post_pk):
    """
    ************ City Page *************
    This page need city specific details.

    1. Airports
    2. Railway Stations
    3. Day Plans
    4. Must see points
    5. Must Try Cuisines
    """
    post_city, city_url = get_redirected(models.CityPost, {'pk': city_post_pk}, {'slug': slug})
    airports = models.Airport.objects.filter(city_post=city_post_pk)
    stations = models.RailwayStation.objects.filter(city_post=city_post_pk)

    # Get all Pay Plans for this City Post
    day_plans = models.DayPlan.objects.filter(city_post=city_post_pk)

    # Get all must_see VisitPoints for the City
    must_see_points = post_city.city.visitpoint_set.filter(must_see=True)

    if city_url:
        return HttpResponseRedirect(city_url)

    return render(request, 'blog/city_post.html',
                  {
                      'city_post': post_city,
                      'airports': airports,
                      'stations': stations,
                      'day_plans': day_plans,
                      'must_see': must_see_points,
                  })
