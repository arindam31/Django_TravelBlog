# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
	search_fields = ['title', ]
	list_display = ['title', 'created_date', 'favourite', 'likes', 'published']
	list_editable = ['favourite', 'published']

# Register your models here.
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment)