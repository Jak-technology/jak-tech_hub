from django.shortcuts import render
# from django.db.models import DjangoModelPermissions

from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from .models import Project, ProjectComment
from .serializers import ProjectSerializer, ProjectCommentSerializer
from .permissions import IsAuthorOrReadOnly, IsStaffOrReadOnly


class ProjectCreateView(generics.CreateAPIView):
    permisssion_classes = [IsStaffOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user)
        else:
            raise PermissionDenied("Error! User must be logged in.")
    
        
class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        comments_queryset = instance.comments.all()
        comments_serializer = ProjectCommentSerializer(comments_queryset, many=True)

        data = serializer.data
        data['comments'] = comments_serializer.data
        return Response(data)