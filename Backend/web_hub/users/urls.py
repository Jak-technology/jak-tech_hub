from django.urls import path
from .views import (UserRegistrationView,
                    UserProfileDetailView,
                    SkillsListView,
                    SpecializationListView,
                    JobTitleListView,
                    UserLoginView,
                    UserLogoutView
                    )



urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('profile/', UserProfileDetailView.as_view(), name='user-profile'),
    path('skills/', SkillsListView.as_view(), name='skills-list'),
    path('specialization/', SpecializationListView.as_view(), name='specialization-list'),
    path('jobtitle/', JobTitleListView.as_view(), name='jobtitle-list'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
]