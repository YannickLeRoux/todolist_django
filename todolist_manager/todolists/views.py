from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,ListView, 
        CreateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ToDoList, Task

from django.contrib.auth import get_user_model
User = get_user_model()


class HomePageView(TemplateView):
    template_name='index.html'


class ToDoListView(LoginRequiredMixin,ListView):
    model = ToDoList
    context_object_name = 'todolists'
    template_name='todolist_list.html'

    def get_queryset(self):
        self.user_lists = ToDoList.objects.filter(user=self.request.user)
        return self.user_lists

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.user_lists = ToDoList.objects.filter(user=self.request.user)
        context['user_lists'] = self.user_lists
        return context


class CreateListView(LoginRequiredMixin,CreateView):
    fields = ('title',)
    model = ToDoList
    template_name = 'todolist_form.html'
    success_url = reverse_lazy('lists')

    def form_valid(self, form):
            form.instance.user = self.request.user
            return super(CreateListView, self).form_valid(form)


class TasksListView(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['description',]
    context_object_name = 'tasks'
    template_name = 'tasks_list.html'
    slug_url_kwarg = 'todolist_slug'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        '''
        Get the Todolist realted to the tasks via the slug 
        '''
        context = super().get_context_data(**kwargs)
        context['todolist'] = get_object_or_404(ToDoList,
                slug=self.kwargs.get('todolist_slug'))
        context['tasks']= Task.objects.filter(
                todolist__slug=self.kwargs['todolist_slug']).order_by('-date_created') 
        return context

    def get_queryset(self):
        queryset = Task.objects.filter(todolist__slug=self.kwargs['slug']).order_by('-date_created')
        return queryset

    def form_valid(self, form):
        task = form.save(commit=False) 
        task.todolist = get_object_or_404(ToDoList,
                slug=self.kwargs.get('todolist_slug'))
        task.save()
        return super(TasksListView, self).form_valid(form)

    def get_success_url(self):
        todolist_slug = self.kwargs.get('todolist_slug')
        return reverse_lazy('tasks', kwargs={'todolist_slug': todolist_slug})


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    slug_url_kwarg = 'todolist_slug'
    pk_url_kwarg = 'task_pk'
    template_name = '../templates/task_confirm_delete.html'


    def get_success_url(self):
        todolist_slug = self.kwargs.get('todolist_slug')
        return reverse_lazy('tasks', kwargs={'todolist_slug': todolist_slug})



