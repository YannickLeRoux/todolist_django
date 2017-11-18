from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from ..views import TasksListView

from ..models import ToDoList, Task


class TasksListViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='Yannick',email='r@hotmail.com',password='testpassword')
        self.todolist = ToDoList.objects.create(title='Test List', user=self.user)
        self.client.login(username='Yannick', password='testpassword')
        self.url = reverse('tasks', kwargs={'slug':'test-list'})
    
    def test_tasks_view_redirect_if_not_logged_in(self):
        self.client.logout()
        url = reverse('tasks', kwargs={'slug':'test-list'})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_task_view_status_code_if_logged_in(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_tasks_url_resolve_to_taskslist_view(self):
        view = resolve('/lists/test-list/')
        self.assertEquals(view.func.view_class, TasksListView)

    # def test_tasks_view_contains_form_inputs(self):
    #     ''' contains 4 inputs text/submit/csrf/checkbox'''
    #     self.assertContains(self.response,'<input',4)
    #     self.assertContains(self.response,'type="text"',1)

    def test_valid_post_create_a_new_task(self):
        self.client.login(username='Yannick', password='testpassword')
        response = self.client.post(self.url, data={'description': 'First activity'})

        self.assertEquals(Task.objects.count(),1)
        new_task = Task.objects.first()
        self.assertEquals(new_task.description,'First activity')
        
        # self.assertEquals(response.status_code, 200)

        # self.assertIn('First activity', response.content.decode())
        self.assertTemplateUsed(response,'tasks_list.html')


