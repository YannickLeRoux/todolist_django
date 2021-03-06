from django.conf import settings
from django.conf.urls import url,include
from django.contrib import admin
from todolists import views

from accounts import views as account_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^signup/$', account_views.SignUpView.as_view(), name='signup'),
    url(r'^login/$',
        auth_views.LoginView.as_view(template_name='accounts/login.html'),
        name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^lists/$', views.ToDoListView.as_view(), name='lists'),
    url(r'^newlist/$', views.CreateListView.as_view(), name='new_list'),
    url(r'^lists/(?P<todolist_slug>[-\w]+)/$', views.TasksListView.as_view(), name='tasks'),
    url(r'^lists/(?P<todolist_slug>[-\w]+)/delete/(?P<task_pk>\d+)/$',views.TaskDeleteView.as_view(),name='delete_task'),

    # url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    # url(r'^accounts/', include('django.contrib.auth.urls')),

]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
