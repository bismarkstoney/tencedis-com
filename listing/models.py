from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
    
class Listing(models.Model):
    title=models.CharField(max_length=250)
    price=models.IntegerField()
    catagories=models.CharField( max_length=50)
    slug=models.SlugField(unique='categories')
    cover_image=models.ImageField(upload_to='listings/')
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    upadated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("listing_details", args=[str(self.slug)])
    
    

