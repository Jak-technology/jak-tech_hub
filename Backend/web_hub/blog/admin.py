from django.contrib import admin
from .models import BlogPost, BlogPostComment


class BlogPostInline(admin.StackedInline):
    model = BlogPost

class BlogPostCommentInline(admin.StackedInline):
    model = BlogPostComment
    extra = 0

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'date_created', 'date_updated')

    inlines = [BlogPostCommentInline]


class BlogPostCommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'date_created', 'date_updated')

admin.site.register(BlogPostComment, BlogPostCommentAdmin)