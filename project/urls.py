"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin

from accounts import urls as accounts_urls
from post import views
from project import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^create_category/', views.create_category, name='create_category'),
    url(r'^update_post/(?P<id>\S+)/$', views.update_post, name='update_post'),
    url(r'^delete_post/(?P<id>\S+)/$', views.delete_post, name='delete_post'),
    url(r'^create_post/$', views.create_post, name='create_post'),
    url(r'^post/like/(?P<id>\S+)/$', views.likes_detail, name='post_like'),
    url(r'^post/dislike/(?P<id>\S+)/$', views.dislikes_detail, name='post_dislike'),
    url(r'^post/post_detail/(?P<info_id>\S+)/$', views.post_detail, name='post_detail'),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^accounts/', include(accounts_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
  + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)



