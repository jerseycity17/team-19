from django.test import TestCase
from django.test.client import Client

from .models import Todo


class TodoTests(TestCase):

    def setUp(self):
        """Lets create one todo that we can use within the tests below"""
        self.example_todo = Todo.objects.create(description="test")

    def test_model_fields_exist(self):
        self.assertTrue(Todo._meta.get_field('user'))
        self.assertTrue(Todo._meta.get_field('description'))
        self.assertTrue(Todo._meta.get_field('due_date'))