from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class ProgramView(TemplateView) :
    template_name = 'progam.html'
    def get_context_data(self, **kwargs):
        context = super(ProgramView, self).get_context_data(self, **kwargs)
        context['data'] = 'ini data yang akan di tampilkan'
        return context
