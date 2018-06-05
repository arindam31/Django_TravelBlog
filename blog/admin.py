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

class CityPostAdmin(admin.ModelAdmin):
    search_fields = ['title', ]
    ordering = ['-created_date', ]
    list_display = ['title', 'created_date', 'published']
    list_editable = ['published', ]

class CityAdmin(admin.ModelAdmin):
    search_fields = ['title', ]

class RestaurantAdmin(admin.ModelAdmin):
    search_fields = ['title', ]
    list_display = ['title', 'city']

class AirportAdmin(admin.ModelAdmin):
    search_fields = ['title', ]
    list_display = ['title', 'city']

class RailwayStationAdmin(admin.ModelAdmin):
    search_fields = ['title', ]
    list_display = ['title', 'city']


# Blog related models

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment, CommentAdmin)

#City related models
admin.site.register(models.CityPost, CityPostAdmin)
admin.site.register(models.City, CityAdmin)
admin.site.register(models.Cuisine)
admin.site.register(models.Airport, AirportAdmin)
admin.site.register(models.Restaurant, RestaurantAdmin)
admin.site.register(models.RailwayStation, RailwayStationAdmin)
