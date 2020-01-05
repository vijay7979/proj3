from django import forms
from . import models # dot signifying the current directory

class createOrder(forms.ModelForm):
	class Meta:
		model = models.Order
		fields =["pizza", "qty_pizza", "toppings","sub", "qty_sub", "additions",
		"pasta", "qty_pasta", "salad", "qty_salad", "dplatter", "qty_dplatter"]