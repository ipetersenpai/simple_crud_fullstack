from django.urls import path
from . import views

urlpatterns = [
    # Read (List and Detail Views)
    path("", views.task_list, name="task-list"),  # List view
    # Create (Add a Task)
    path("create/", views.create_task, name="task-create"),
]
