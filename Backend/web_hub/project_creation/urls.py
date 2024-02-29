from django.urls import path
from .views import (ProjectCreateView,
                    ProjectListView,
                    ProjectDetailView,
#                     ProjectUpdateView,
#                     ProjectDeleteView,
)

urlpatterns = [
    path('project/create/', ProjectCreateView.as_view(), name='create-project'),
    path('project/list/', ProjectListView.as_view(), name='list-project'),
    path('project/list/<int:id>/', ProjectDetailView.as_view(), name='project-detail'),
    # path('project/update/<int:id>/', ProjectUpdateView.as_view(), name='update-project'),
    # path('project/delete/<int:id>/', ProjectDeleteView.as_view(), name='delete-project'),
]