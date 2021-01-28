import json
import pdb

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIRequestFactory, APITestCase

from blog.api import PostCreateApi
from blog.models import Post



class BlogApiTests(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_one_element_all_posts(self):
        """
        Test: Create one post. Expecting one element to be present in response.
        """
        user = User.objects.create(first_name="Firstname")
        Post.objects.create(author=user, title="Test Post", text="Some text", slug='test_post', pk=1)
        _ = reverse('api_post_list')
        request = self.factory.get('/posts')
        view = PostCreateApi().as_view()
        response = view(request)
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(response.data))



