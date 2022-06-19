from .models import *
from django import forms
from django.forms import Forms

class TaskForm(forms.Forms):
	class meta:
		model = Task
		fields = "__all__"