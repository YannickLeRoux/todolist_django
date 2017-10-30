from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from ..views import HomePageView, ToDoListView

class HomeTests(TestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)
    
    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_root_url_resolve_to_homepage_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, HomePageView)

    def test_home_view_contains_link_to_signup_page(self):
        signup_url = reverse('signup')
        self.assertContains(self.response, 'href="{0}"'.format(signup_url))

    def test_home_view_contains_link_to_login_page(self):
        login_url = reverse('login')
        self.assertContains(self.response, 'href="{0}"'.format(login_url))

class TodoListsPageTests(TestCase):

    def setUp(self):
        url = reverse('lists')
        self.response = self.client.get(url)
    
    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_lists_url_resolve_to_lists_view(self):
        view = resolve('/lists/')
        self.assertEquals(view.func.view_class, ToDoListView)

    def test_list_view_contains_link_to_tasks_page(self):
        tasks_url = reverse('tasks')
        self.assertContains(self.response, 'href="{0}"'.format(tasks_url))

    def test_lists_view_contains_link_to_create_new_list(self):
        new_list_url = reverse('new_list')
        self.assertContains(self.response, 'href="{0}"'.format(new_list_url))

    # def test_unlogged_user_cant_see_lists_page(self):
    #     pass

    # def test_lists_page_contains_a_list_of_todolist(self):
    #     pass




