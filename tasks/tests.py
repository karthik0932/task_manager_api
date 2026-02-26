from django.test import TestCase
from .models import Task

class TaskTest(TestCase):
    def test_create_task(self):
        task = Task.objects.create(title="Test", description="DevOps test")
        self.assertEqual(task.title, "Test")
