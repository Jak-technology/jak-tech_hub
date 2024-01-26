from django.shortcuts import render

from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import BlogPostSerializer, BlogPostCommentSerializer
from .models import BlogPost, BlogPostComment
from project_creation.permissions import IsAuthorOrReadOnly


class BlogCreateView(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def perform_create(self, serializer):
        try:
            serializer.save(author=self.request.user)
        except Exception as e:
            raise ValueError("Error! User must be logged in.")


class BlogListView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogDetailView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        comments_queryset = instance.comments.all()
        comments_serializer = BlogPostCommentSerializer(comments_queryset, many=True)

        data = serializer.data
        data['comments'] = comments_serializer.data
        
        return Response(data)


class BlogUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'id'


class BlogDeleteView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'id'