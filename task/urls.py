from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="task-list"),
    path("create/", views.task_create, name="task-create"),
    path("delete/<int:task_id>/", views.delete_task, name="delete-task"),
    path("task/success/", views.task_success, name="task-success"),
]
