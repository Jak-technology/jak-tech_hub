
from django.urls import path
from .views import ServicesListCreateView, get_choices
from . import views


urlpatterns = [
    path('api/services/', ServicesListCreateView.as_view(), name='services'),
    path('api/choices/', views.get_choices, name='choices'),
]