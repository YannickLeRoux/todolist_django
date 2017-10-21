from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from ..views import HomePageView

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_root_url_resolve_to_homepage_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, HomePageView)


