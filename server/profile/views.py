from django.shortcuts import render
from .models import UserProfile
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['POST'])
def sync_clerk_user(request):
    data = request.data
    clerk_id = data.get("clerk_id")
    
    user_profile, created = UserProfile.objects.get_or_create(clerk_id=clerk_id, defaults={
        "username": data.get("username"),
        "email": data.get("email")
    })
    
    if not created:
        user_profile.username = data.get("username")
        user_profile.email = data.get("email")
        user_profile.save()
        
    return Response({"message": "User profile created successfully"}, status=status.HTTP_201_CREATED)