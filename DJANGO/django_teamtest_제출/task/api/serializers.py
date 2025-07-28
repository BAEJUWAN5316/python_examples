from rest_framework import serializers
from task.models import Task
from django.db.models import QuerySet
from django.conf import settings
from django.contrib.auth import get_user_model

class TaskSerializer(serializers.ModelSerializer):
    def is_overdue():
        pass

    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "completed",
            "due_date",
            "created_at"
        ]