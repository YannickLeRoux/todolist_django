from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from ..views import TasksListView

from ..models import ToDoList, Task


class TasksListViewTests(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='Yannick',email='rasyann@hotmail.com',password='dancehall')
        todolist = ToDoList.objects.create(title='Test List', user=user)
        task = Task.objects.create(description='J ai ca a faire',
                todolist=todolist)
        url = reverse('tasks', kwargs={'pk':1})
        self.response = self.client.get(url)
    
    def test_tasks_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_tasks_url_resolve_to_taskslist_view(self):
        view = resolve('/lists/1/')
        self.assertEquals(view.func.view_class, TasksListView)









