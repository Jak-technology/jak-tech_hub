from django.contrib import admin
from .models import BlogPost, BlogPostComment


admin.site.register(BlogPost)

admin.site.register(BlogPostComment)
