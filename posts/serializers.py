from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Post, Vote


class PostSerializer(serializers.ModelSerializer):
    #user = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all())
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Post
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = '__all__'
