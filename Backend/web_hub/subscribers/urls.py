from django.urls import path
from .views import *


urlpatterns = [
    path('subscriber/create/', CreateSubscriberAPIView.as_view(), name='create-subscriber'),
]