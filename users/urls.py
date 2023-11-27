from django.urls import path

from users.views import login, registration, profile, logout
from records.views import therapist_profile

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('therapist/', therapist_profile, name='therapist_profile'),
]
