# -*- coding: utf-8 -*-
"""
This module contains admin related classes.
"""

from __future__ import unicode_literals

from django.contrib import admin

from blog import models


class PostAdmin(admin.ModelAdmin):
    """Post admin class"""
    search_fields = ['title', ]
    list_display = ['title', 'created_date', 'favourite', 'likes',
                    'published']
    list_editable = ['favourite', 'published']


class CommentAdmin(admin.ModelAdmin):
    """Comment admin class"""
    list_display = ['detail', 'post', 'created_date']
    ordering = ['-created_date', ]  # -ve sign for ordering in desc


class CityPostAdmin(admin.ModelAdmin):
    """CityPost admin class"""
    search_fields = ['title', ]
    ordering = ['-created_date', ]  # This is show by latest date on top
    list_display = ['title', 'created_date', 'published']
    list_editable = ['published', ]


class CityAdmin(admin.ModelAdmin):
    """City admin class"""
    search_fields = ['title', ]


class RestaurantAdmin(admin.ModelAdmin):
    """Restaurant admin class"""
    search_fields = ['title', ]
    list_display = ['title', 'city']


class AirportAdmin(admin.ModelAdmin):
    """Airport admin class"""
    search_fields = ['title', ]
    list_display = ['title', 'city']


class RailwayStationAdmin(admin.ModelAdmin):
    """Railway Station admin class"""
    search_fields = ['title', ]
    list_display = ['title', 'city']


class DayPlanAdmin(admin.ModelAdmin):
    """Day Plan admin class"""

    # Note : __str__ gives the output of the __str__ method defined under the model
    search_fields = ['__str__']
    list_display = ['__str__', 'no_of_days', ]


class VisitPointAdmin(admin.ModelAdmin):
    """Visit Point admin class"""
    search_fields = ['title', ]
    list_display = ['title', 'city', 'timings']


# Blog related models

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment, CommentAdmin)

# City related models
admin.site.register(models.CityPost, CityPostAdmin)
admin.site.register(models.City, CityAdmin)
admin.site.register(models.Cuisine)
admin.site.register(models.Airport, AirportAdmin)
admin.site.register(models.Restaurant, RestaurantAdmin)
admin.site.register(models.RailwayStation, RailwayStationAdmin)
admin.site.register(models.DayPlan, DayPlanAdmin)
admin.site.register(models.VisitPoint, VisitPointAdmin)
