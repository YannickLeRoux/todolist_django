from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', views.CustomLoginView.as_view(),name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name="logout"),
    url(r'^$', views.SignUp.as_view(), name="signup"),
]
