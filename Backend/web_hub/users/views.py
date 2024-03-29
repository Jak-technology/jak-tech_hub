from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import UserProfile, Skills, Specialization, JobTitle
from .serializers import (UserRegistrationSerializer,
                          UserProfileSerializer,
                          SkillsSerializer,
                          SpecializationSerializer,
                          JobTitleSerializer
                         )


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        """ Overrides the default 'create' method provided by 'CreateAPIView' """
        
        #Initializes the serializer with the request data
        serializer = self.get_serializer(data=request.data)
        
        # Validates the serializer data
        serializer.is_valid(raise_exception=True) 
           
        # Calls the 'perform_create' method to create a new 
        # object using the serializer data.
        self.perform_create(serializer)
        
        # Retrieves success headers using 'get_success_headers'
        headers = self.get_success_headers(serializer.data)

        return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED, headers=headers)


class UserLoginView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserLogoutView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)


class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class SkillsListView(generics.ListAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = [permissions.IsAuthenticated]


class SpecializationListView(generics.ListAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    permission_classes = [permissions.IsAuthenticated]


class JobTitleListView(generics.ListAPIView):
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer
    permission_classes = [permissions.IsAuthenticated]


class SkillsCreateView(generics.CreateAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = [permissions.IsAuthenticated]


class SpecializationCreateView(generics.CreateAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    permission_classes = [permissions.IsAuthenticated]


class JobTitleCreateView(generics.CreateAPIView):
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer
    permission_classes = [permissions.IsAuthenticated]


class SkillsDeleteView(generics.DestroyAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Skill deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class SpecializationDeleteView(generics.DestroyAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Specialization deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class JobTitleDeleteView(generics.DestroyAPIView):
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": f"{instance} deleted successfully."}, status=status.HTTP_204_NO_CONTENT)