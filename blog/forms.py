from django import forms
from . import models

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'text', 'author']

