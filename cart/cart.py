from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart(object):

	def __init__(self, request):
		"""
		Initialize the cart
		"""
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			# save an empty cart in the session
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart

	def add(self, product, quantity=1, update_quantity=False):
		"""
		Add a product to the cart or update its quantity
		"""
		product_id = str(product.id)
		if product_id not in self.cart:
			self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
		if update_quantity:
			self.cart[product_id]['quantity'] = quantity
		else:
			self.cart[product_id]['quantity'] += quantity
		self.save()

		# notes
		# product_id is used as key in cart's content dic. str because django uses
		# JSON to serialize session data, and JSON only allows str key names.

	def save(self):
		# mark the session as modified to ensure its saved
		self.session.modified = True

	def remove(self, product):
		"""
		Remove a product from the cart
		"""
		product_id = str(product.id)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()

	def __iter__(self):
		"""
		Iterate over the items in the cart and get the products from the database
		"""
		product_ids = self.cart.keys()

		# get the product objects and add them to the cart
		# using id__in means select the products where the id is in product_ids (its a shortcut)
		products = Product.objects.filter(id__in=product_ids)

		cart = self.cart.copy()

		for product in products:
			cart[str(product.id)]['product'] = product

		for item in cart.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] = item['price'] * item['quantity']
			yield item

		# using dunderscore as we're creating a custom len function
		def __len__(self):
			"""
			count all items in the cart
			"""
			return sum(item['quantity'] for item in self.cart.values())

		# calculate the total cost of the items in the cart
		def get_total_price(self):
			return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

		# clear the cart session
		def clear(self):
			# remove cart from session
			del self.session(settings.CART_SESSION_ID)
			self.save()







