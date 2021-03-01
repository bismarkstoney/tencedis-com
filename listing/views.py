from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView, DetailView, DeleteView
from .models import Listing
# Create your views here.
class ListingsListView(ListView):
    model=Listing
    template_name='listing/listings.html'

    