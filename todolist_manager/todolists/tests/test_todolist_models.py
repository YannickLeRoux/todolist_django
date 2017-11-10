from django.contrib.auth.models import User
from django.test import TestCase

from ..models import ToDoList, Task



class TestsTodoListModel(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(username='Yan',email='r@gmail.com',password='testpassword')
        self.todolist= ToDoList.objects.create(title='Test List', user=self.user)

    def test_title_display(self):
        self.assertEquals(str(self.todolist),'Test List')

    def test_slug(self):
        self.assertEquals(self.todolist.slug,'test-list')


class TestsTaskModel(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(username='Yan',email='r@gmail.com',password='testpassword')
        self.todolist= ToDoList.objects.create(title='Test List', user=self.user)
        self.task= Task.objects.create(description='Jai ca a faire',
                todolist=self.todolist)

    def test_description_display(self):
        self.assertEquals(str(self.task),'Jai ca a faire')

