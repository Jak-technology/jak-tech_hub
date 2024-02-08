from django.contrib import admin
from .models import Project, ProjectComment



class ProjectInline(admin.StackedInline):
    model = Project

class ProjectCommentInline(admin.StackedInline):
    model = ProjectComment
    extra = 0

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'date_created', 'date_updated')

    inlines = [ProjectCommentInline]


#@admin.register(ProjectComment)
class ProjectCommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'date_created', 'date_updated')

admin.site.register(ProjectComment, ProjectCommentAdmin)