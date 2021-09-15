from profiles import serializers
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from profiles import models, serializers, permissions

# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.updateOwnProfile, )
