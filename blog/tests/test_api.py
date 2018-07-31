from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from blog.models import Post
from rest_framework.test import APIRequestFactory, APITestCase
import pdb
from blog.api import ListPostApi
import json


class BlogApiTests(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_empty_array_all_posts(self):
        """
        Test: No post present in db, expecting empty arrays in response
        """
        request = self.factory.get('/api/v1/posts/')
        url = reverse('api_post_list')
        response = ListPostApi().get(request)
        self.assertEqual(200, response.status_code)
        self.assertEqual([], response.data)

    def test_one_element_all_posts(self):
        """
        Test: One post create. Expecting one element to be present in response
        """
        user = User.objects.create(first_name="Firstname")
        Post.objects.create(author=user, title="Test Post", text="Some text", slug='test_post', pk=1)
        request = self.factory.get('/api/v1/posts/')
        url = reverse('api_post_list')
        response = ListPostApi().get(request)
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(response.data))



