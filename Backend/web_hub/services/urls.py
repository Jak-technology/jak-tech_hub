
from django.urls import path
from .views import ServicesListCreateView

urlpatterns = [
    path('api/services/', ServicesListCreateView.as_view(), name='services'),
]