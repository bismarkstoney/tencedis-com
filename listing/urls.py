from django.urls import path, re_path
from .views import ListingsListView 



urlpatterns = [
     path('', ListingsListView.as_view(), name='listings' )
]