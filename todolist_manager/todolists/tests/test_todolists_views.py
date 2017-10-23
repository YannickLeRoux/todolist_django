from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from ..views import HomePageView

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


