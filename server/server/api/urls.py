from django.urls import path
from profile.urls import urlpatterns as  profile_urls

urlpatterns = [
    path('', profile_urls)
]
