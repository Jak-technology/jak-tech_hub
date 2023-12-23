from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title', 'date_created']

    def __str__(self):
        """ String for representing the Model object. """
        return f'{self.title} - {self.author}'

    def get_absolute_url(self):
        """ Returns the URL to access a particular blog post """
        return reverse('blog-post', args=[str(self.id)])


class BlogPostComment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['author', 'date_created']

    def __str__(self):
        """ String for representing the Model object. """
        return self.content

    def get_absolute_url(self):
        """ Returns the URL to access a particular BlogPost comment """
        return reverse('comment-detail', args=[str(self.id)])


