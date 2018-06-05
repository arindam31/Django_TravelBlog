# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
	search_fields = ['title', ]
	list_display = ['title', 'created_date', 'favourite', 'likes',
                            'published']
	list_editable = ['favourite', 'published']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['detail', 'post', 'created_date']
    ordering = ['-created_date', ] # -ve sign for ordering in desc order in admin comment date column

# Register your models here.
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment, CommentAdmin)

admin.site.register(models.CityPost)
admin.site.register(models.City)
admin.site.register(models.Cuisine)
admin.site.register(models.Address)

