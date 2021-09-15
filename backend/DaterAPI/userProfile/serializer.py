from rest_framework import serializers
from userProfile import models


"""Serializer of user object"""


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }
