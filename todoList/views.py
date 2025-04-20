from django.shortcuts import render
from todoList.models import Task

# Create your views here.
def todos(request):
	todo_list = Task.objects.all()

	return render(request, 'todos/todo_list.html', {'todo_list': todo_list})

def add_task(request):
	pass