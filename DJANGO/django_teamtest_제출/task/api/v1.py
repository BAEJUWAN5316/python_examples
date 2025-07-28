from django.urls import path
from task.models import Task
from task.api.serializers import TaskSerializer
from rest_framework.viewsets import ModelViewSet

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

task_list_or_new = TaskViewSet.as_view({
    "get": "list", "post":"create"
})

task_detail_or_edit_or_delete = TaskViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

urlpatterns= [
    path("tasks/", task_list_or_new),
    path("tasks/<id:int>", task_detail_or_edit_or_delete),
]



