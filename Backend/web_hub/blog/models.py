from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default="images/blog_images/default.png/", upload_to="images/blog_images/uploads/%Y/%m-%d")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['title', 'date_created']
        
    def save(self, *args, **kwargs):
        if not self.author_id and hasattr(self, '_request') and self._request.user.is_authenticated:
            self.author = self._request.user
        super().save(*args, **kwargs)

    def __str__(self):
        """ String for representing the Model object. """
        return f'{self.title} - {self.author}'

    def get_absolute_url(self):
        """ Returns the URL to access a particular blog post """
        return reverse('blog-post', args=[str(self.id)])



class BlogPostComment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['author', 'date_created']

    def __str__(self):
        """ String for representing the Model object. """
        return self.content

    def get_absolute_url(self):
        """ Returns the URL to access a particular BlogPost comment """
        return reverse('comment-detail', args=[str(self.id)])


