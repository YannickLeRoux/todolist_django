from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from ..views import CreateListView

class CreateListViewTest(TestCase):
    '''
    TODO: test a valid form submision redirect to lists
    '''
    def setUp(self):
        url = reverse('new_list')
        self.response = self.client.get(url)
    
    def test_createlist_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_createlists_url_resolve_to_CreateListView(self):
        view = resolve('/newlist/')
        self.assertEquals(view.func.view_class, CreateListView)
