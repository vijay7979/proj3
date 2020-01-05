from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Topping(models.Model):
	topping = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.topping}"

#For Addition the pricing is consistent so price can be included here; as opposed to Topping
class Addition(models.Model):
	category = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=5, decimal_places=2, default=0.50)

	def __str__(self):
		return f"{self.category}"

class Pizza(models.Model):
	category = models.CharField(max_length=64)
	size = models.CharField(max_length=20, choices=[('Small', 'Small'), ('Large', 'Large')], default='Large')
	num_toppings = models.IntegerField(choices=[(0, 'None'), (1, 'One'), (2,'Two'),(3,'Three')], default=0)
	price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

	def __str__(self):
			return f"ID: {self.id}, {self.size} {self.category} Pizza with {self.num_toppings} toppings"

class Sub(models.Model):
	category = models.CharField(max_length=64)
	size = models.CharField(max_length=20, choices=[('Small', 'Small'), ('Large', 'Large')], default='Large')
	price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

	def __str__(self):
		return f"{self.size} {self.category} Sub - {self.price}"

class Pasta(models.Model):
	category = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	#problem as Order is defined below Pasta, so considered 'not defined'
	#orders = models.ManyToManyField(Order, blank=True, related_name="pastas")

	def __str__(self):
		return f"{self.category} {self.price}"

class Salad(models.Model):
	category = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

	def __str__(self):
		return f"{self.category}"

class DinnerPlatter(models.Model):
	category = models.CharField(max_length=64)
	size = models.CharField(max_length=20, choices=[('Small', 'Small'), ('Large', 'Large')], default='Large')
	price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

	def __str__(self):
		return f"{self.category}({self.size})"

#model item and quantity. item details are in their respective models.
class Order(models.Model):
	pizza = models.ForeignKey(Pizza, blank=True, null=True, on_delete=models.CASCADE)
	qty_pizza = models.IntegerField(default=1, blank=True, null=True)
	toppings = models.ManyToManyField(Topping, blank=True)
	sub = models.ForeignKey(Sub, blank=True, null=True, on_delete=models.CASCADE)
	qty_sub = models.IntegerField(default=1, blank=True, null=True)
	additions = models.ManyToManyField(Addition, blank=True)
	pasta = models.ForeignKey(Pasta, blank=True, null=True, on_delete=models.CASCADE)
	qty_pasta = models.IntegerField(default=1, blank=True, null=True)
	salad = models.ForeignKey(Salad, blank=True, null=True, on_delete=models.CASCADE)
	qty_salad = models.IntegerField(default=1, blank=True, null=True)
	dplatter = models.ForeignKey(DinnerPlatter, blank=True, null=True, on_delete=models.CASCADE)
	qty_dplatter = models.IntegerField(default=1, blank=True, null=True)
	created_at = models.DateTimeField(default=datetime.now)
	created_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

	def __str__(self):
		return f"Order ID {self.id}, {self.pizza}"

	def additions_price(self):
		additions = self.additions.all()
		additions_price = 0
		for addition in additions:
			additions_price += addition.price
		return additions_price

	# this is done in view, as need to check 'None' or not, but is here as example
	def tot_price(self):
		total_price=0
		if not self.pizza is None:
			total_price += (self.pizza.price * self.qty_pizza)
		if not self.sub is None:
			total_price += (self.sub.price * self.qty_sub)
		if not self.pasta is None:
			total_price += (self.pasta.price * self.qty_pasta)
		if not self.salad is None:
			total_price += (self.salad.price * self.qty_salad)
		if not self.dplatter is None:
			total_price += (self.dplatter.price * self.qty_dplatter)
		return total_price


		
	