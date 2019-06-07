from django.urls import path

from . import views
urlpatterns = [
    path('helloworld/', views.helloWorld),
    path('', views.taskList, name='Task-list'),
    path('yourname/<str:name>', views.yourName, name='your-name'),
]
