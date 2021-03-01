from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# from .models import Category   

class Category(models.Model):
    title=models.CharField( max_length=100)
    image=models.ImageField( upload_to='categories/')

    def __str__(self):
        return self.title
    
class Listing(models.Model):
    title=models.CharField(max_length=250)
    price=models.IntegerField()
    categories=models.ForeignKey(Category, on_delete=models.CASCADE)
    slug=models.SlugField(unique='categories')
    cover_image=models.ImageField(upload_to='listings/')
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    upadated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("listing_details", args=[str(self.slug)])

    
    

