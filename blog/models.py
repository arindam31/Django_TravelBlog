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

	def get_absolute_url(self):
		return reverse(
			'post_details',
			kwargs={'slug': self.post.slug, 'post_pk': self.post.pk }
			)

	def __str__(self):
		return self.detail

class City(models.Model):
	"""
	City is just a name.
	"""
	name = models.CharField(max_length=100)
	class Meta:
		verbose_name_plural = "cities"

	def __str__(self):
		return self.name

class CityPost(models.Model):
	"""
	A city post is an article about a City.
	"""
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



class Address(models.Model):
	"""
	This is an abstract class. Everything is an address .
	Example: Airport, Station, Restaurent, or a place of interest.
	"""
	title = models.CharField(max_length=200)
	street = models.TextField()
	city = models.ForeignKey(City)
	pincode = models.PositiveIntegerField(null=True, blank=True)
	city_post = models.ForeignKey(CityPost, blank=True, null=True)

	class Meta:
		abstract = True

	def __str__(self):
		return self.title


class VisitPoint(Address):
	"""

	A VisitPoint is a point in the city , the tourist can visit.
	Its has some extra fields apart from Address attribs:

	1. Timings: Usually visit points has timing limitations.
	2. must_see boolean helps filtering/marking a point as must see or
	casual/low prioriry.
	3. Intro: Short one liner introduction.

	"""
	timings = models.CharField(blank=True, max_length=100)
	must_see = models.BooleanField(default=False)
	intro = models.CharField(default='', blank=True, max_length=200)


class DayPlan(models.Model):
	"""
	A day plan is a possible combination for a tourist. He can plan his visit
	using anyone. Attribs are:

	1. No of days : Total duration of stay.
	2. Which City Post.
	3. What City Points to visit.

	"""
	no_of_days = models.PositiveIntegerField()
	city_post = models.ForeignKey(CityPost, blank=True, null=True)
	visit_points = models.ManyToManyField(VisitPoint, blank=True)

	def __str__(self):
		return '_'.join([str(self.no_of_days) , self.city_post.title])

	def plan_heading(self):
		"""
		This method is needed to create the Day pLan heading. It's
		directly called from template like: day_plan.plan_heading

		Format: N Nights D Days
		"""
		if self.no_of_days == 1:
			return '1 Day'
		elif self.no_of_days == 2:
			return '{} Night {} Days'.format(self.no_of_days-1, self.no_of_days)
		else:
			return '{} Nights {} Days'.format(self.no_of_days-1, self.no_of_days)


class Airport(Address):
	pass

class Restaurant(Address):
	pass

class RailwayStation(Address):
	pass



class Cuisine(models.Model):
	"""
	Cuisine class for Dishes.
	1. Title
	2. Description
	3. Single Image
	4. Which City Post
	5. Which Restaurent #TODO
	"""
	title = models.CharField(max_length=100)
	description = models.TextField()
	pic = models.ImageField(upload_to = 'media/')
	city_post = models.ForeignKey(CityPost, blank=True, null=True)

