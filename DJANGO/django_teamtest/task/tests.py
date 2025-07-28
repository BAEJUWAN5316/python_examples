from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from django.db import models
from rest_framework.test import APITestCase
from rest_framework import status
import json
from .models import Task
from .serializers import TaskSerializer
from .views import TaskViewSet

class TaskModelTest(TestCase): # 10점
    def setUp(self):
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task",
            due_date=timezone.now().date() + timedelta(days=1)
        )

    def test_task_creation(self):
        # Task 객체가 올바르게 생성되었는지 확인 (1점)
        self.assertTrue(isinstance(self.task, Task))
        self.assertEqual(str(self.task), "Test Task")

    def test_task_ordering(self):
        # Task 객체들이 생성 시간의 역순으로 정렬되는지 확인 (3점)
        Task.objects.create(
            title="Another Task",
            description="This is another test task",
            due_date=timezone.now().date() + timedelta(days=2)
        )
        tasks = Task.objects.all()
        self.assertEqual(tasks.first().title, "Another Task")
        self.assertEqual(tasks.last().title, "Test Task")

    def test_is_overdue(self):
        # is_overdue 메서드가 올바르게 작동하는지 확인 (3점)
        self.assertFalse(self.task.is_overdue())
        self.task.due_date = timezone.now().date() - timedelta(days=1)
        self.task.save()
        self.assertTrue(self.task.is_overdue())

    def test_field_constraints(self):
        # Task 모델의 필드 제약 조건을 확인 (3점)
        task = Task.objects.create(
            title="Test Task",
            description="This is a test task",
            due_date=timezone.now().date()
        )
        
        self.assertEqual(task._meta.get_field("title").max_length, 200)
        self.assertFalse(task.completed)
        self.assertIsNotNone(task.created_at)
        self.assertIsInstance(task._meta.get_field("due_date"), models.DateField)

class TaskSerializerTest(TestCase): # 10점
    def setUp(self):
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task",
            due_date=timezone.now().date() + timedelta(days=1)
        )

    def test_task_serializer_contains_expected_fields(self):
        # TaskSerializer가 필요한 필드를 모두 포함하고 있는지 확인 (3점)
        serializer = TaskSerializer(instance=self.task)
        data = serializer.data
        
        self.assertIn('title', data)
        self.assertIn('description', data)
        self.assertIn('completed', data)
        self.assertIn('due_date', data)
        self.assertIn('created_at', data)
        self.assertIn('is_overdue', data)

    def test_task_serializer_is_overdue_field(self):
        # TaskSerializer의 is_overdue 필드가 올바르게 작동하는지 확인 (3점)
        serializer = TaskSerializer(instance=self.task)
        data = serializer.data
        self.assertFalse(data['is_overdue'])
        
        self.task.due_date = timezone.now().date() - timedelta(days=1)
        self.task.save()
        
        serializer = TaskSerializer(instance=self.task)
        data = serializer.data
        self.assertTrue(data['is_overdue'])

    def test_task_serializer_validation(self):
        # TaskSerializer의 유효성 검사가 올바르게 작동하는지 확인 (2점)
        valid_data = {
            'title': 'New Task',
            'description': 'New description',
            'due_date': timezone.now().date() + timedelta(days=1),
            'completed': False
        }
        serializer = TaskSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())

    def test_task_serializer_created_at_readonly(self):
        # created_at 필드가 읽기 전용인지 확인 (2점)
        serializer = TaskSerializer()
        self.assertIn('created_at', serializer.fields)
        self.assertTrue(serializer.fields['created_at'].read_only)

class TaskAPITest(APITestCase): # 20점
    def setUp(self):
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task",
            due_date=timezone.now().date() + timedelta(days=1)
        )

    def test_task_list_api(self):
        # Task 목록 API가 올바르게 작동하는지 확인 (2점)
        url = reverse('tasks:task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_task_list_api_filtering(self):
        # Task 목록 API의 필터링이 올바르게 작동하는지 확인 (4점)
        completed_task = Task.objects.create(
            title="Completed Task",
            description="This is a completed task",
            due_date=timezone.now().date() + timedelta(days=1),
            completed=True
        )
        new_task = Task.objects.create(
            title="New Task",
            description="This is a new task",
            due_date=timezone.now().date() + timedelta(days=2)
        )
        
        url = reverse('tasks:task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # 완료되지 않은 작업이 먼저 나와야 함
        results = response.data['results']
        self.assertEqual(results[0]['title'], 'New Task')
        self.assertEqual(results[1]['title'], 'Test Task')
        
        # completed 필터링 테스트
        response = self.client.get(url, {'completed': 'true'})
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Completed Task')

    def test_task_detail_api(self):
        # Task 상세 조회 API가 올바르게 작동하는지 확인 (2점)
        url = reverse('tasks:task-detail', args=[self.task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task.title)

    def test_task_create_api(self):
        # Task 생성 API가 올바르게 작동하는지 확인 (3점)
        url = reverse('tasks:task-list')
        data = {
            'title': 'New API Task',
            'description': 'Created via API',
            'due_date': timezone.now().date() + timedelta(days=1),
            'completed': False
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(Task.objects.order_by('-created_at').first().title, 'New API Task')

    def test_task_update_api(self):
        # Task 수정 API가 올바르게 작동하는지 확인 (3점)
        url = reverse('tasks:task-detail', args=[self.task.id])
        data = {
            'title': 'Updated Task',
            'description': 'Updated description',
            'due_date': timezone.now().date(),
            'completed': True
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')
        self.assertEqual(self.task.completed, True)

    def test_task_partial_update_api(self):
        # Task 부분 수정 API가 올바르게 작동하는지 확인 (3점)
        url = reverse('tasks:task-detail', args=[self.task.id])
        data = {'completed': True}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.task.refresh_from_db()
        self.assertEqual(self.task.completed, True)
        self.assertEqual(self.task.title, 'Test Task')  # 다른 필드는 변경되지 않아야 함

    def test_task_delete_api(self):
        # Task 삭제 API가 올바르게 작동하는지 확인 (3점)
        url = reverse('tasks:task-detail', args=[self.task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

class TaskURLsTest(TestCase): # 10점
    def setUp(self):
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task",
            due_date=timezone.now().date() + timedelta(days=1)
        )

    def test_task_list_url(self):
        # Task 목록 URL이 올바른지 확인 (2점)
        url = reverse("tasks:task-list")
        self.assertEqual(url, "/api/tasks/")

    def test_task_detail_url(self):
        # Task 상세 조회 URL이 올바른지 확인 (2점)
        url = reverse("tasks:task-detail", args=[self.task.id])
        self.assertEqual(url, f"/api/tasks/{self.task.id}/")

    def test_task_create_url(self):
        # Task 생성 URL이 목록 URL과 동일한지 확인 (2점)
        url = reverse("tasks:task-list")
        self.assertEqual(url, "/api/tasks/")

    def test_task_update_url(self):
        # Task 수정 URL이 상세 URL과 동일한지 확인 (2점)
        url = reverse("tasks:task-detail", args=[self.task.id])
        self.assertEqual(url, f"/api/tasks/{self.task.id}/")

    def test_task_delete_url(self):
        # Task 삭제 URL이 상세 URL과 동일한지 확인 (2점)
        url = reverse("tasks:task-detail", args=[self.task.id])
        self.assertEqual(url, f"/api/tasks/{self.task.id}/")

class TaskViewSetTest(TestCase): # 10점
    def setUp(self):
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task",
            due_date=timezone.now().date() + timedelta(days=1)
        )

    def test_task_viewset_queryset_filtering(self):
        # TaskViewSet의 get_queryset이 올바르게 필터링하는지 확인 (5점)
        completed_task = Task.objects.create(
            title="Completed Task",
            description="This is a completed task",
            due_date=timezone.now().date() + timedelta(days=1),
            completed=True
        )
        
        from .views import TaskViewSet
        from rest_framework.request import Request
        from django.test import RequestFactory
        
        factory = RequestFactory()
        request = factory.get('/api/tasks/')
        
        viewset = TaskViewSet()
        viewset.request = Request(request)
        viewset.action = 'list'
        
        queryset = viewset.get_queryset()
        
        # 완료되지 않은 작업만 포함되어야 함
        self.assertEqual(queryset.count(), 1)
        self.assertEqual(queryset.first().title, "Test Task")

    def test_task_viewset_overdue_filtering(self):
        # TaskViewSet의 overdue 필터링이 올바르게 작동하는지 확인 (5점)
        overdue_task = Task.objects.create(
            title="Overdue Task",
            description="This is an overdue task",
            due_date=timezone.now().date() - timedelta(days=1)
        )
        
        from rest_framework.test import APIRequestFactory
        from .views import TaskViewSet
        
        factory = APIRequestFactory()
        request = factory.get('/api/tasks/', {'overdue': 'true'})
        
        viewset = TaskViewSet()
        viewset.request = request
        viewset.action = 'list'
        
        queryset = viewset.get_queryset()
        
        # 만기일이 지난 작업만 포함되어야 함
        overdue_titles = [task.title for task in queryset]
        self.assertIn("Overdue Task", overdue_titles)
        self.assertNotIn("Test Task", overdue_titles)