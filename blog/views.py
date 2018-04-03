# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import forms


# Create your views here.
def post_list(request):
    posts =models.Post.objects.filter(created_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_details(request, post_pk):
    post = models.Post.objects.get(pk=post_pk)
    return render(request, 'blog/post_details.html', {'post': post })

def create_post(request):
    form = forms.BlogPostForm()
    if request.method == 'POST':
        form = forms.BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('Well done!')


