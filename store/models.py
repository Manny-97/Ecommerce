from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# Category table
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    # def get_absolute_url(self):
    #     return reverse("store: category_list", args=[self.slug])
    

    def __str__(self):
        return self.name

# Product table
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='product_creator', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')      # Not storing the image in the db, we just storing the link to the image
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('store: product_detail', args=[self.slug])
    