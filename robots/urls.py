from django.urls import path

from .views import create_robot

urlpatterns = [
    path('v1/create_robot/', create_robot, name='create_robot'),
]
