from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Skills, Specialization, JobTitle


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UserRegistrationSerializer(serializers.ModelSerializer):
    """ User Serializer class """
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['name']


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['name']


class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTitle
        fields = ['title']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    gender = serializers.CharField(required=False, allow_blank=True, max_length=10)
    date_of_birth = serializers.DateField()
    phone_number = serializers.CharField(max_length=15)
    skills = SkillsSerializer(many=True)
    specialization = SpecializationSerializer(many=True)
    job_title = JobTitleSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = '__all__'