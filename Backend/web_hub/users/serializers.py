from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Skills, Specialization, JobTitle


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
    skills = SkillsSerializer(many=True)
    specialization = SpecializationSerializer(many=True)
    job_title = JobTitleSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = '__all__'