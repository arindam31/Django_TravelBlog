# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = RichTextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	published = models.BooleanField(default=False)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def get_absolute_url(self):
		return reverse(
			'post_details', 
			kwargs={'post_pk':self.id}
			)


	def __str__(self):
		return self.title

