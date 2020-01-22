from .cart import Cart 

# set current cart into request context so that its globally available.
# "cart" is then available to all templates.
# also added to context processors option in settings.
def cart(request):
	return {'cart': Cart(request)} 