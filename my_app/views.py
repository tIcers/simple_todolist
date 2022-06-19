from django.shortcuts import render
from .models import Task
from .forms import *
# Create your views here.

def todolist(request):
	all_tasks = Task.objects.all()

	form = TaskForm()
	context={'all_tasks':all_tasks,'form':form}

	return render(request, 'my_app/todolist.html',context)