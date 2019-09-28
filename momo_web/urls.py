"""momo_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('momo.urls')),
    path('job/', include('job.urls')),
<<<<<<< HEAD
    path('user/', include('allauth.urls')),
=======
>>>>>>> aab0717fe2eb36de1db09b20755749f0ef111192
]



if settings.DEBUG:
    urlpatterns += [
        path(r'^static/(?P<path>.*)$', views.serve)
    ]
