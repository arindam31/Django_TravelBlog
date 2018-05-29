# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client
from django.urls import reverse

from .models import Post

class TestPostModel(TestCase):

    def setUp(self):
        user = User.objects.create(first_name="Firstname")
        self.a_post = Post(author=user, title="Test Post", text="Some text", slug='test_post', pk=1)

    def test_post_absolute_url(self):
        abs_url = self.a_post.get_absolute_url()
        self.assertEqual(u'/post/1/test_post/', abs_url)

    def test_get_images_from_post_description(self):
        result = self.a_post.get_images_from_post_description()
        self.assertEqual(False, result,
            'Expected response boolean False, instead received: %s' % result)


class TestBlogViews(TestCase):

    def setUp(self):
        user = User.objects.create(first_name="Firstname")
        self.a_post = Post(author=user, title="Test Post",
            text="Some text", slug='test_post', pk=1,
            favourite=True)
        self.client = Client()

    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(200, response.status_code)

