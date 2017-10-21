from django.conf.urls import url
from . import views

app_name = 'todolists'

urlpatterns = [
        url(r'^$',views.ToDoListView.as_view(), name='lists'),
        ]
