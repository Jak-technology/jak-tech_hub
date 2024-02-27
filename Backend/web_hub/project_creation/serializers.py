from rest_framework import serializers

from users.serializers import UserSerializer

from .models import Project, ProjectComment


class ProjectSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'author', 'title', 'content', 'image', 'date_created', 'date_updated']


class ProjectCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = ProjectComment
        fields = '__all__'