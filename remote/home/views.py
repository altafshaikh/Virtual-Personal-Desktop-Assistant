from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.views.generic import CreateView, TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'
