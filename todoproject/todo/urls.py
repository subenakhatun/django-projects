from django.urls import path
from .import views

app_name = 'todo'

urlpatterns = [
    path('',views.task_list, name='task_list'),
    # path('add/',views.task_list, name='task_list'),
    # path('add/',views.task_list, name='task_list'),
    # path('add/',views.task_list, name='task_list'),
]