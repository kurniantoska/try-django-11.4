from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views import View
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import RestaurantLocation
from .forms import RestaurantLocationCreateForm

class RestaurantListView(LoginRequiredMixin, ListView) :
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantDetailView(DetailView) :
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)


class RestaurantCreateView(LoginRequiredMixin, CreateView) :
    form_class = RestaurantLocationCreateForm
    template_name = 'form.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context

class RestaurantUpdateView(LoginRequiredMixin, UpdateView) :
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurants/detail-update.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Edit {}'.format(self.get_object().name)
        return context

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)
