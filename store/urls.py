"""
URL configuration for store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from records.views import index, lastrecords, addrecord, therapists, therapist_profile, record_update, cancel_record

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('lastrecords/', lastrecords, name='lastrecords'),
    path('users/', include('users.urls', namespace='users')),
    path('addrecord/', addrecord, name='addrecord'),
    path('therapists/', therapists, name='therapists'),
    path('therapists/<int:therapist_id>/', therapist_profile, name='therapist_profile'),
    path('record_update/', record_update, name='record_update'),
    path('cancel_record/<int:record_id>/', cancel_record, name='cancel_record'),

    path('api/', include('records.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
