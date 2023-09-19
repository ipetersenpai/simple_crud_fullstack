from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.


# Render all the task list
def task_list(request):
    tasks = Task.objects.all()
    return render(request, "task/task_detail.html", {"tasks": tasks})


# Create a new task
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tast-list")
    else:
        form = TaskForm()

    return render(request, "task_create.html", {"form": form})
