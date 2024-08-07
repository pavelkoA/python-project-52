from task_manager.statuses.models import Status
from django.urls import reverse_lazy
from django.db.models import ProtectedError
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import CustomLoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class StatusesListView(CustomLoginRequiredMixin,
                       ListView):
    model = Status
    template_name = 'statuses/statuses_list.html'
    context_object_name = 'statuses'
    extra_context = {
        'title': _('Statuses')
    }


class StatusCreateView(CustomLoginRequiredMixin,
                       SuccessMessageMixin,
                       CreateView):
    model = Status
    template_name = 'statuses/create.html'
    fields = ['name']
    success_message = _('Status successfully created')
    success_url = reverse_lazy('statuses_list')
    extra_context = {
        'title': _('Create status'),
        'button_text': _('Create'),
    }


class StatusUpdateView(CustomLoginRequiredMixin,
                       SuccessMessageMixin,
                       UpdateView):
    model = Status
    template_name = 'statuses/update.html'
    fields = ['name']
    success_message = _('Status successfully changed')
    success_url = reverse_lazy('statuses_list')
    extra_context = {
        'title': _('Change status'),
        'button_text': _('Change'),
    }


class StatusDeleteView(CustomLoginRequiredMixin,
                       SuccessMessageMixin,
                       DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_message = _('Status successfully delete')
    success_url = reverse_lazy('statuses_list')
    protected_message = _(
        'It is not possible to delete the status, it is in use'
    )
    protected_url = reverse_lazy('statuses_list')
    extra_context = {
        'title': _('Delete status'),
        'button_text': _('Delete'),
    }

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)
