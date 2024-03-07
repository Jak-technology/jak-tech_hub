from django.urls import path
from .views import (BlogCreateView,
                    BlogListView,
                    BlogDetailView,
)



urlpatterns = [
    path('blog/create/', BlogCreateView.as_view(), name='create-blog'),
    path('blog/list/', BlogListView.as_view(), name='list-blog'),
    path('blog/list/<int:id>/', BlogDetailView.as_view(), name='blog-detail'),
]