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
       
    def test_description_display(self):
        task= Task.objects.create(description='Jai ca a faire',
                todolist=self.todolist)
        self.assertEquals(str(task),'Jai ca a faire')

    def test_saving_and_retrieving_items(self):
        first_task = Task()
        first_task.description = 'The first (ever) list item'
        first_task.todolist = self.todolist
        first_task.save()

        second_task = Task()
        second_task.description = 'Item the second'
        second_task.todolist = self.todolist
        second_task.save()

        saved_tasks = Task.objects.all()
        self.assertEqual(saved_tasks.count(), 2)

        first_saved_task = saved_tasks[0]
        second_saved_task = saved_tasks[1]
        self.assertEqual(first_saved_task.description, 'The first (ever) list item')
        self.assertEqual(second_saved_task.description, 'Item the second')





