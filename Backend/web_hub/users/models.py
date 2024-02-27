from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              blank=True,
                              default='M',
                              help_text='Select Your Gender'
                            )
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    skills = models.ManyToManyField('Skills')
    job_title = models.ManyToManyField('JobTitle')
    specialization = models.ManyToManyField('Specialization')
    location = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    class Meta:
        ordering = ['user__first_name', 'user__last_name']
    
    def __str__(self):
        """ String for representing the Model object. """
        return f'{self.user.first_name} - {self.job_title.all().first()}'

    def get_absolute_url(self):
        """ Returns the URL to access a user profile """
        return reverse('user-profile', args=[str(self.id)])


class Skills(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        """ String for representing the Model object. """
        return f"{self.name}"

    def get_absolute_url(self):
        """ Returns the URL to access a particular skill """
        return reverse('skill-detail', args=[str(self.id)])


class Specialization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        """ String for representing the Model object. """
        return f"{self.name}"

    def get_absolute_url(self):
        """ Returns the URL to access a particular specialization """
        return reverse('specialization-detail', args=[str(self.id)])


class JobTitle(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        """ String for representing the Model object. """
        return f"{self.title}"

    def get_absolute_url(self):
        """ Returns the URL to access a particular job title """
        return reverse('job-title', args=[str(self.id)])


class SocialMediaHandles(models.Model):
    user_profile = models.OneToOneField('UserProfile', on_delete=models.CASCADE)
    x = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    tiktok = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Social Media Handles for {self.user_profile}"