from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class ToDoList(models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(default='',allow_unicode=True, unique=True)
    user = models.ForeignKey(User, related_name='lists')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)



class Task(models.Model):
    description = models.CharField(max_length=128)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True,blank=True,null=True)
    todolist = models.ForeignKey(ToDoList,related_name='tasks')
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.description
