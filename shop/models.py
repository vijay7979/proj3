from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# reverse method allows the bulding of URLs by their name and passing optional parameters
from django.urls import reverse

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=64) # add "db_index=True"? 
	slug = models.SlugField(max_length=64, unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		# using namespace "shop" to refer to the url for product_list_by_category
		return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
	category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
	name = models.CharField(max_length=64) # db_index?
	slug = models.SlugField(max_length=64) # db_index?
	image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
	description = models.TextField(blank=True)
	size = models.CharField(max_length=20, choices=[('Small', 'Small'), ('Large', 'Large')], default='Large')
	price = models.DecimalField(max_digits=10, decimal_places=2)
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	created_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

	class Meta:
		ordering = ('name',)
		index_together = (('id', 'slug'),)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:product_detail', args=[self.id, self.slug])

	
	