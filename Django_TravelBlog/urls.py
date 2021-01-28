"""Django_TravelBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers  # All this for our new version of API v2

from blog import views
from blog import api

# Routers help us, not explicitly create urls , like we did for v1.
# Routers will create the URLs automatically for us.

router = routers.SimpleRouter()
router.register('posts', api.PostViewSet)
router.register('comments', api.CommentViewSet)

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'', include('blog.urls')),
                  url(r'^accounts/', include('allauth.urls')),
                  url(r'^ckeditor/', include('ckeditor_uploader.urls')),
                  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  url(r'^api/v1/posts/', include('blog.api_url')),
                  url(r'^api/v2/', include(router.urls)),

              ] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT) + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT)

handler500 = views.error_500
handler404 = views.error_404

# To change the admin default title
admin.site.site_header = "TheBongTravellers !"
admin.site.site_title = "TheBongTravellers !"
