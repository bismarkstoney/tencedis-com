from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView, DetailView, DeleteView
from listing .models import Listing,Category
# Create your views here.
class HomeListView(ListView):
    model=Listing
    template_name="pages/home.html"
    context_object_name='listings'

class CategoriesListView(ListView):
    model=Category
    template_name="pages/home.html"
    context_object_name='listings'

    def get_queryset(self, *args, **kwargs):
        return Category.objects.filter(title__icontains=self.kwargs.get('categories'))
    