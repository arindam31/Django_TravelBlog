# -*- coding: utf-8 -*-
import re
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.template.defaultfilters import slugify


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = RichTextField()
	short_intro = models.TextField(default='')
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	published = models.BooleanField(default=False)
	likes = models.PositiveIntegerField(default=0)
	favourite = models.BooleanField(default=False)
	tags = models.ManyToManyField(Tag, blank=True)
	slug = models.SlugField(max_length=100, blank=False)

	def publish(self):
		self.published_date = timezone.now()
		self.published = True
		self.save()

	#def get_absolute_url(self):
	#	return reverse(
	#			'post_details',
	#		kwargs={'post_pk':self.id}
	#			)

	def get_absolute_url(self):
		return reverse(
			'post_details',
			kwargs={'slug': self.slug, 'post_pk': self.id }
			)


	def get_images_from_post_description(self):
	    des = self.text
	    #first_image = re.findall('(?<=src=")https.*jpg', des)
	    images = re.findall('(?<=src=").*jpg', des)
	    images = sorted(images)
	    if images:
	        return images[0]
	    return False


	def __str__(self):
		return self.title


class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='comments')
	detail = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ['-created_date'] # Negative sign is for descending order
		                             # in model.objects.all response

	def approve(self):
		self.approve_comment = True
		self.save()

	def get_absolute_url(self):
		return reverse(
			'post_details',
			kwargs={'slug': self.post.slug, 'post_pk': self.post.pk }
			)

	def __str__(self):
		return self.detail

class City(models.Model):
	name = models.CharField(max_length=100)
	class Meta:
		verbose_name_plural = "cities"

	def __str__(self):
		return self.name

class Address(models.Model):
	title = models.CharField(max_length=200)
	street = models.TextField()
	city = models.ForeignKey(City)
	pincode = models.PositiveIntegerField(blank=True)

	class Meta:
		abstract = True

	def __str__(self):
		return self.title

class DayPlan(models.Model):
	no_of_days = models.PositiveIntegerField()

	def __str__(self):
		return self.no_of_days

class Airport(Address):
	pass

class Restaurant(Address):
	pass

class RailwayStation(Address):
	pass


class CityPost(models.Model):
	title = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	city = models.ForeignKey(City)
	best_month = models.DateField(max_length=30)
	intro = models.TextField()
	description = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published = models.BooleanField(default=False)
	slug = models.SlugField(max_length=100, blank=False, default=title)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse(
			'city_post',
			kwargs={'slug': self.slug, 'city_post_pk': self.id }
			)


class Cuisine(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	pic = models.ImageField(upload_to = 'media/')
