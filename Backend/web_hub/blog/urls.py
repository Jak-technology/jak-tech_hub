from django.urls import path
from .views import (alt_apiview,
                    BlogCreateView,
                    BlogListView,
                    BlogDetailView,
                    BlogUpdateView,
                    BlogDeleteView,
)



urlpatterns = [
    path('blog/', alt_apiview, name='blogs-list'),
    path('blog/create/', BlogCreateView.as_view(), name='create-blog'),
    path('blog/list/', BlogListView.as_view(), name='list-blog'),
    path('blog/list/<int:id>', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/update/<int:id>', BlogUpdateView.as_view(), name='blog-update'),
    path('blog/delete/<int:id>', BlogDeleteView.as_view(), name='blog-delete'),
]