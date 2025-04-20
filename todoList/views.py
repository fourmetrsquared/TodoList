from django.shortcuts import render, redirect
from todoList.models import Task
from todoList.forms import TaskForm

# Create your views here.
def todos(request):
	todo_list = Task.objects.all()

	return render(request, 'todos/todo_list.html', {'todo_list': todo_list})

def add_task(request):
	if request.method == "POST":
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('task_list')
	else:
		form = TaskForm()
	return render(request, 'todos/add_task.html', {'form': form})