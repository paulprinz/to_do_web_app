from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('list', views.list, name='list'),
    path('addTask', views.addTask, name='addTask'),
    path("changeAchieved", views.changeAchieved, name='changeAchieved'),
    path("deleteTask", views.deleteTask, name='deleteTask'),
    path("editTask", views.editTask, name='editTask')
]


