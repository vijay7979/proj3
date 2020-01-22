from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,21)]

class CartAddProductForm(forms.Form):
	quantity = forms.TypedChoiceField(
								choices=PRODUCT_QUANTITY_CHOICES,
								coerce=int)
	# this allows us to indicate whether the quantity has to be added to any existing 
	# quantity in the cart(False). Or whether the field has to be updated with the given 
	# quantity(True). HiddenInput widget used so as not to display this field to the user.
	update = forms.BooleanField(required=False,
								initial=False,
								widget=forms.HiddenInput)