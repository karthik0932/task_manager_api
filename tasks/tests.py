from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task


class TaskTest(TestCase):
    def test_create_task_model(self):
        task = Task.objects.create(title="Test", description="DevOps test")
        self.assertEqual(task.title, "Test")


class TaskAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_task(self):
        data = {
            "title": "API Task",
            "description": "Testing create"
        }
        response = self.client.post("/api/tasks/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_tasks(self):
        Task.objects.create(title="Sample Task")
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        task = Task.objects.create(title="Delete Task")
        response = self.client.delete(f"/api/tasks/{task.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_failure_example(self):
        self.assertEqual(1, 2)