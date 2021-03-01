from django.urls import path
from .views import  HomeListView, CategoriesListView


urlpatterns = [
     path('', HomeListView.as_view(), name="home"),
     path('categories/<str:categories>/', CategoriesListView.as_view(), name="category"),
]