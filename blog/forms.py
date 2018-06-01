from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from . import models

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'text', 'tags', 'author', 'slug']
    helper = FormHelper()
    helper.form_class = 'form-group'
    helper.layout = Layout(
        Field('title', css_class='form-control mt-2 mb-3'),
        Field('text', rows="3", css_class='form-control mb-3'),
        Field('author', css_class='form-control mb-3'),
        Field('tags', css_class='form-control mb-3'),
        Field('slug', css_class='form-control'),
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['detail', ]

    helper = FormHelper()
    helper.form_class = 'form-group'
    helper.layout = Layout(
        Field('detail', rows="3", css_class='form-control'),
            )

