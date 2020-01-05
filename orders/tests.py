from django.test import Client, TestCase

from . models import Topping, Addition, Pizza, Sub, Pasta, Salad, DinnerPlatter, Order

# Note: If calling foreign key, the instance has to be created first as the test database is empty.
# It calls Models but has no data.

# following should be in settings.py so that don't have to manually change databases but 
# haven't figured it out yet.
# import sys
# if 'test' in sys.argv:
#     DATABASES['default'] = {
#         'ENGINE': 'django.db.backends.postgresql',
#         #'NAME': 'mydatabase'
#     }

class ModelsTestCase(TestCase):

	def setUp(self):

		# Create Pizza
		P1 = Pizza.objects.create(category="Chilli", size="L", num_toppings=2, price=50)
		P2 = Pizza.objects.create(category="Banana", size="S", num_toppings=1, price=25)
		S1 = Sub.objects.create(category="Funny", size="Large", price=100)

	def test_pizza_created(self):
		p = Pizza.objects.get(category="Chilli")
		q = Pizza.objects.get(category="Banana")
		self.assertEqual(p.price, 50)
		self.assertEqual(q.category, "Banana")

	def test_online_order(self):
		c = Client()
		response = c.get("/online_order")
		self.assertEqual(response.status_code, 200)

		# It expects me to be logged in. else it gives response as NoneType since context 
		# doesn't get to the page. So remove login_required for online_order and that should 
		# solve the 302 code issue also. And it worked!
		self.assertEqual(response.context["subs"].count(), 1)
		self.assertEqual(response.context["pizzas"].count(), 2)

	def test_valid_order(self):
		P3 = Pizza.objects.create(category="Bugs", size="S", num_toppings=1, price=412)
		S3 = Sub.objects.create(category="Italian", size="Large", price=220)

		# following line would only work if created_by in Order model is removed as its linked to Users
		order1 = Order.objects.create(pizza=P3)
		order1.save()

		c = Client()

		# the slash in front of order.id is required
		response = c.get(f"/{order1.id}")
		self.assertEqual(response.status_code, 200)

		# context is from views.order
		self.assertEqual(response.context["total_price"], 412)




