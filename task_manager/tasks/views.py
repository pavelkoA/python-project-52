from task_manager.tasks.models import Task
from task_manager.tasks.filters import TaskFilter
from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import CustomLoginRequiredMixin, AuthorPermissionMixin
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)


class TasksListView(CustomLoginRequiredMixin,
                    FilterView,
                    ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    filterset_class = TaskFilter
    context_object_name = 'tasks'
    extra_context = {
        'title': _('Tasks'),
        'button_text': _('Show')
    }


class TaskShowView(CustomLoginRequiredMixin,
                   DetailView):
    model = Task
    template_name = 'tasks/task_show.html'
    context_object_name = 'task'
    extra_context = {
        'title': _('View a task')
    }


class TaskCreateView(CustomLoginRequiredMixin,
                     SuccessMessageMixin,
                     CreateView):
    model = Task
    template_name = 'tasks/create.html'
    fields = ['name', 'description', 'status', 'labels', 'executor']
    success_url = reverse_lazy('tasks_list')
    success_message = _('Task successfully created')
    extra_context = {
        'title': _('Create task'),
        'button_text': _('Create'),
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(CustomLoginRequiredMixin,
                     SuccessMessageMixin,
                     UpdateView):
    model = Task
    template_name = 'tasks/update.html'
    fields = ['name', 'description', 'status', 'labels', 'executor']
    success_url = reverse_lazy('tasks_list')
    success_message = _('Task successfully changed')
    extra_context = {
        'title': _('Task change'),
        'button_text': _('Change'),
    }


class TaskDeleteView(AuthorPermissionMixin,
                     CustomLoginRequiredMixin,
                     SuccessMessageMixin,
                     DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks_list')
    success_message = _('Task successfully delete')
    author_permission_message = _('The task can be deleted only by its author')
    author_permission_url = reverse_lazy('tasks_list')
    extra_context = {
        'title': _('Delete task'),
        'button_text': _('Delete'),
    }
