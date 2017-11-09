from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from ..views import CreateListView

class CreateListViewTest(TestCase):
    '''
    TODO: test a valid form submision redirect to lists
    '''
    def setUp(self):
        '''
        creating an user and log in 
        '''
        User.objects.create_user(username='Yan',email='r@hotmail.com',password='testpassword')
        self.client.login(username='Yan',password='testpassword')
        url = reverse('new_list') 
        self.response = self.client.get(url)
    
    def test_createlist_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_createlists_url_resolve_to_CreateListView(self):
        view = resolve('/newlist/')
        self.assertEquals(view.func.view_class, CreateListView)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_form_inputs(self):
        '''
        The view must contain five inputs: csrf, username, email,
        password1, password2
        '''
        self.assertContains(self.response, '<input', 2)
        self.assertContains(self.response, 'type="text"', 1)

    # tester que la liste cree corespond bien a l user de la request

