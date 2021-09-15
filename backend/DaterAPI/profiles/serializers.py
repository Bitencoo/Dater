from django.db.models import fields
from rest_framework import serializers
from profiles import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer a user profile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

        def create(self, validated_data):
            """Create and return a new user"""
            user = models.UserProfile.objects.create_user(
                email=validated_data['email'],
                name=validated_data['name'],
                password=validated_data['password']
            )

        def update(self, validated_data):
            """Handle updtaing user account"""
            if 'password' in validated_data:
                password = validated_data.pop('password')
                self.set_password(password)

            return super().update(self, validated_data)
