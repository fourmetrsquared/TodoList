from django import forms
from todoList.models import Task

class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['title', 'description']