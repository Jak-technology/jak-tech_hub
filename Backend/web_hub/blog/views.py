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


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
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


class BlogPostCommentCreateView(generics.CreateAPIView):
    serializer_class = BlogPostCommentSerializer

    def perform_create(self, serializer):
        blog_post = BlogPost.objects.get(id=self.kwargs['id'])
        serializer.save(blogpost=blog_post)

    def post(self, request, *args, **kwargs):                
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(f"serializer.data: {serializer.data}")
        print(f"Serializer.valadated_data: {serializer.validated_data}")
        try:
            blog_post = BlogPost.objects.get(id=self.kwargs['id'])
            print(blog_post)
            blog_post_comment = BlogPostComment.objects.create(
                blogpost = blog_post,
                content = serializer.validated_data['content'],
                email = serializer.validated_data['email'],
                author = serializer.validated_data['author']
            )
            print(f"BlogPostComment saved successfully!: {blog_post}")
            return Response(serializer.data)
        except Exception as e:
            print("Error, comment not saved: ", e)
            return Response({"message": "Comment was not saved"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        