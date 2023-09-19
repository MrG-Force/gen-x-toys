from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name
    
class Toy(models.Model):
    YEAR_CHOICES = [(r, r) for r in range(1965, 1994)]
    
    category = models.ForeignKey(Category, related_name='toys', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='toys_images/', blank=True, null=True)
    stock = models.PositiveIntegerField()
    manufacturer = models.CharField(max_length=255, blank=True, null=True)
    release_year = models.IntegerField(choices=YEAR_CHOICES, default=1970)
    created_by = models.ForeignKey(User, related_name='toys', on_delete=models.CASCADE)
    date_time_created = models.DateTimeField(auto_now_add=True,)
    
    class Meta:
        ordering = ('title',)
        
    def __str__(self):
        return self.title

