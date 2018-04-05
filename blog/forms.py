from django import forms
from ckeditor.fields import RichTextFormField
from . import models

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'text', 'author']

    content = RichTextFormField()

