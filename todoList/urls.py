from tkinter.font import names

from django.urls import path
from todoList import views

urlpatterns = [
	path('todos', views.todos, name = 'task_list'),
	path('add_task', views.add_task, name = 'add_task')
]