from django.urls import path
from .views import sync_clerk_user

urlpatterns = [
    path('sync-clerk-user/', sync_clerk_user, name='sync_clerk_user')
]