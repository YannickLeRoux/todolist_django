from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView):
    template_name='index.html'


class ToDoListView(LoginRequiredMixin,ListView):
    template_name='todolist_list.html'

# Create your views here.
