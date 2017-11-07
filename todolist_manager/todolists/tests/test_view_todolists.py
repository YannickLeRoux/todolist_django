from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from ..views import HomePageView, ToDoListView, CreateListView

class TodoListsPageTests(TestCase):

    def setUp(self):
        url = reverse('lists')
        self.response = self.client.get(url)
    
    def test_todolist_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_lists_url_resolve_to_lists_view(self):
        view = resolve('/lists/')
        self.assertEquals(view.func.view_class, ToDoListView)

    def test_lists_view_contains_link_to_tasks_page(self):
        tasks_url = reverse('tasks')
        self.assertContains(self.response, 'href="{0}"'.format(tasks_url))

    def test_lists_view_contains_link_to_create_new_list(self):
        new_list_url = reverse('new_list')
        self.assertContains(self.response, 'href="{0}"'.format(new_list_url))

    # def test_unlogged_user_cant_see_lists_page(self):
    #     pass

    # def test_lists_page_contains_a_list_of_todolist(self):
    #     pass

    # def new_user_get_empty_message(self):
    #     self.user = User.objects.create()


