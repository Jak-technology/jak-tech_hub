from django.contrib import admin
from .models import Project, ProjectComment


admin.site.register(Project)

admin.site.register(ProjectComment)
