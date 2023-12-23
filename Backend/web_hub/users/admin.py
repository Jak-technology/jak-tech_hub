from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import JobTitle, UserProfile, Skills, Specialization


admin.site.register(JobTitle)
admin.site.register(UserProfile)
admin.site.register(Skills)
admin.site.register(Specialization)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profiles'


class CustomUserAdmin(UserAdmin):
    #list_display = ('gender', )
    inlines = [UserProfileInline]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)