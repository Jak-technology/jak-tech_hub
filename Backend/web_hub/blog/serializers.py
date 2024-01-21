from rest_framework import serializers

from users.serializers import UserSerializer

from .models import BlogPost, BlogPostComment


class BlogPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = BlogPost
        fields = '__all__'