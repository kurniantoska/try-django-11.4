from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth import get_user_model
from django.views.generic import DetailView

from menus.models import Item
from restaurants.models import RestaurantLocation
# Create your views here.

User = get_user_model()
class ProfileDetailView(DetailView):
    def get_object(self):
        username = self.kwargs.get("username")
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        user = context['user']
        query = self.request.GET.get('q')
        item_exists = Item.objects.filter(user=user).exists()
        qs = RestaurantLocation.objects.filter(owner=user).search(query)
        if item_exists and qs.exists():
            context['locations'] = qs
        return context
