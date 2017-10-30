from django.shortcuts import render
from django.views.generic import TemplateView,ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ToDoList


class HomePageView(TemplateView):
    template_name='index.html'


class ToDoListView(ListView):
    model = ToDoList
    context_object_name = 'todolists'
    template_name='todolist_list.html'

class CreateListView(CreateView):
    fields = ('title',)
    model = ToDoList
    template_name = 'todolist_form.html'
    success_url = 'lists'


# Create your views here.
