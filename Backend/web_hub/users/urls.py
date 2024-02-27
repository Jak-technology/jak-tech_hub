from django.urls import path
from .views import (UserRegistrationView,
                    UserProfileListCreateView,
                    UserProfileDetailView,
                    SkillsListView,
                    SpecializationListView,
                    JobTitleListView,
                    UserLoginView,
                    UserLogoutView,
                    SkillsCreateView,
                    SpecializationCreateView,
                    JobTitleCreateView,
                    SkillsDeleteView,
                    SpecializationDeleteView,
                    JobTitleDeleteView
                    )



urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
]

# ListView patterns
urlpatterns += [
    path('api/profiles/', UserProfileListCreateView.as_view(), name='user-profile-list'),
    path('api/profiles/<int:pk>', UserProfileDetailView.as_view(), name='user-profile'),
    path('api/skills/', SkillsListView.as_view(), name='skills-list'),
    path('api/specialization/', SpecializationListView.as_view(), name='specialization-list'),
    path('api/jobtitle/', JobTitleListView.as_view(), name='jobtitle-list'),
]

# CreateView patterns
urlpatterns += [
    path('api/skills/create/', SkillsCreateView.as_view(), name='create-skills'),
    path('api/specialization/create/', SpecializationCreateView.as_view(), name='create-specialization'),
    path('api/jobtitle/create/', JobTitleCreateView.as_view(), name='create-jobtitle'),
]

# DeleteView patterns
urlpatterns += [
    path('api/skills/<int:pk>/delete/', SkillsDeleteView.as_view(), name='delete-skills'),
    path('api/specialization/<int:pk>/delete/', SpecializationDeleteView.as_view(), name='delete-specialization'),
    path('api/jobtitle/<int:pk>/delete/', JobTitleDeleteView.as_view(), name='delete-jobtitle'),
]