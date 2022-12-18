from django.contrib import admin
from . models import *
from .forms import ElephantForm

# Register your models here.
from django.contrib.auth.models import Group
admin.site.unregister(Group)

class NotesAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'description']
    list_filter = ['user', 'title',]
admin.site.register(Notes, NotesAdmin)

class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject', 'short_title', 'description','due', 'is_finished']
    list_filter = ['user', 'title', 'is_finished', 'due', ]
admin.site.register(Homework, HomeworkAdmin)

class TodoAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'is_finished']
    list_filter = ['user', 'title','is_finished']
admin.site.register(Todo, TodoAdmin)
