from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


# Create your views here.


# Create a new task
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task-list")
    else:
        form = TaskForm()

    return render(request, "task/task_create.html", {"form": form})


# Render all the task list
def task_list(request):
    tasks = Task.objects.all()
    return render(request, "task/task_detail.html", {"tasks": tasks})


# Update a task
def update_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        # Handle the case where the task does not exist (optional)
        pass

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)  # Use TaskForm instead of form
        if form.is_valid():
            form.save()
            return redirect("task-list")
    else:
        form = TaskForm(instance=task)  # Use TaskForm instead of form

    return render(request, "task/task_update.html", {"form": form, "task": task})


# Delete a task
def delete_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        task.delete()
    except Task.DoesNotExist:
        # Handle the case where the task does not exist (optional)
        pass

    return redirect("task-list")


# Render the task success page
def task_success(request):
    return render(request, "task/task_success.html")
