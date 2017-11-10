from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from ..views import TasksListView

from ..models import ToDoList, Task


class TasksListViewTests(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='Yannick',email='r@hotmail.com',password='testpassword')
        todolist = ToDoList.objects.create(title='Test List', user=user)
        Task.objects.create(description='J ai ca a faire',todolist=todolist)
        self.client.login(username='Yannick', password='testpassword')
        url = reverse('tasks', kwargs={'slug':'test-list'})
        self.response = self.client.get(url)
    
    def test_tasks_view_redirect_if_not_logged_in(self):
        self.client.logout()
        url = reverse('tasks', kwargs={'slug':'test-list'})
        self.response = self.client.get(url)
        self.assertEquals(self.response.status_code, 302)

    def test_task_view_status_code_if_logged_in(self):
        self.assertEquals(self.response.status_code, 200)

    def test_tasks_url_resolve_to_taskslist_view(self):
        view = resolve('/lists/test-list/')
        self.assertEquals(view.func.view_class, TasksListView)

    def test_tasks_view_contains_link_to_new_task(self):
        new_task_url = reverse('new_task', kwargs={'slug':'test-list'})
        self.assertContains(self.response,'href="{0}"'.format(new_task_url))












