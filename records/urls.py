from django.urls import path, include
from rest_framework.routers import DefaultRouter

from records.views import index, ClientsViewSet, EventsViewSet

app_name = 'records'
router = DefaultRouter()
router.register(r'clients', ClientsViewSet)
router.register(r'events', EventsViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('', include(router.urls))
]
