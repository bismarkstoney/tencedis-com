from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView, DetailView, DeleteView
from listing .models import Listing
# Create your views here.
class HomeListView(ListView):
    model=Listing
    template_name="pages/home.html"
    context_object_name='listings'