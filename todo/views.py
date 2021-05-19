from django.shortcuts import render
from .models import Task
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task']
        labels = {'text': " add "}
        

def index(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            HttpResponseRedirect("/")
            
    else:
        form = TaskForm()
    
    
    
    context = {
        "tasks": tasks,
        "form": form
    }
    return render(request, r"todo\index.html", context)
        
        
    
def delete(request, task_id):
    task = Task.objects.get(pk = task_id)
    task.delete()
    return HttpResponseRedirect(reverse("todo:index"))
    
