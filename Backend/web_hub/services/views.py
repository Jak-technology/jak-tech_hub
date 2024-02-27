from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import Services
from .serializers import ServicesSerializer



class ServicesListCreateView(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]