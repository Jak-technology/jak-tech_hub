from rest_framework import serializers

from users.serializers import UserSerializer

from .models import BlogPost, BlogPostComment

        
class BlogPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)    
    class Meta:
        model = BlogPost
        fields = ['id', 'author', 'title', 'description', 'content', 'image', 'date_created', 'date_updated']


class BlogPostCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = BlogPostComment
        fields = ['id', 'content', 'author', 'date_created', 'date_updated']