from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import datetime
from . import forms

#from django.urls import reverse

from .models import Pizza, Sub, Topping, Addition, Order, Pasta, Salad, DinnerPlatter

# Create your views here.

#@login_required(login_url="login")
def order_index(request):

	context = {
		"orders": Order.objects.all()
	}

	return render(request, "orders/order_index.html", context)

# creating order form using model forms
#@login_required(login_url="login")
def create_order(request):
	if request.method == "POST":
		form = forms.createOrder(request.POST)
		if form.is_valid:
			# save to database
			# commit is false so that created_by attribute can be added
			instance = form.save(commit=False)
			instance.created_by = request.user
			instance.save()
			return HttpResponseRedirect("order_index")
	else:
		# create the form from createOrder class defined in forms.py
		form = forms.createOrder()
	context = {
		"form": form
	}
	return render(request, "orders/create_order.html", context)

# create and process order form using manual html
# @login_required(login_url="login")
def online_order(request):

	# process the incoming order 
	if request.method == "POST":
		try:
			if request.POST["pz"] != "0" :
				pizza_id = int(request.POST["pz"])
				pizza = Pizza.objects.get(pk=pizza_id)
			else:
				pizza=None
			if request.POST["sb"] != "0" :
				sub_id = int(request.POST["sb"])
				sub = Sub.objects.get(pk=sub_id)
			else:
				sub=None
			if request.POST["ps"] != "0" :
				pasta_id = int(request.POST["ps"])
				pasta = Pasta.objects.get(pk=pasta_id)
			else: 
				pasta = None
			if request.POST["sld"] != "0" :
				salad_id = int(request.POST["sld"])
				salad = Salad.objects.get(pk=salad_id)
			else:
				salad=None
			if request.POST["dpl"] != "0" :
				dplatter_id = int(request.POST["dpl"])
				dplatter = DinnerPlatter.objects.get(pk=dplatter_id)
			else:
				dplatter=None
		except KeyError:
			return render(request, "orders/error.html", {"message": "No selection"})
		except Pizza.DoesNotExist:
			return render(request, "orders/error.html", {"message": "That Pizza is not available"})
		except Topping.DoesNotExist:
			return render(request, "orders/error.html", {"message": "That Topping is not available"})
		except Pasta.DoesNotExist:
			return render(request, "orders/error.html", {"message": "That Pasta is not available"})

		# check if order is being submitted without selecting anything
		if pizza is None and sub is None and pasta is None and salad is None and dplatter is None:
			return render(request, "orders/error.html", {"message": "At least one item must be selected"})

		try:
			order.update(pizza= pizza, sub= sub, pasta= pasta, salad= salad, dplatter= dplatter)
			order.save()
		except:
			order = Order(pizza= pizza, sub= sub, pasta= pasta, salad= salad, dplatter= dplatter,
				created_by=request.user)
			order.save()

		context = {"order_id": order.id, "pizza": pizza, "sub": sub, "pasta": pasta, "salad": salad, "dplatter": dplatter}

		return render(request, "orders/order_confirmation.html", context)

	# render the order form	if its a GET request
	else:
		context = {
			"pizzas": Pizza.objects.all(),
			"toppings": Topping.objects.all(),
			"subs": Sub.objects.all(),
			"additions": Addition.objects.all(),
			"pastas": Pasta.objects.all(),
			"salads": Salad.objects.all(),
			"dplatters": DinnerPlatter.objects.all()
		}

		return render(request, "orders/online_order.html", context)


#@login_required(login_url="login")
# the order_id variable is captured as order.id and passed in by order_index template to urls.
# urls.py captures with <>, ensures its an integer, and names it order_id.
def order(request, order_id):

	try:
		order = Order.objects.get(pk=order_id)
	except Order.DoesNotExist:
		raise Http404("Order does not exist.")

	try:
		i=0
		additions = order.additions.all()
		for addition in additions:
			i+=1
		num_additions=i
	except:
		pass

	pizza_price=0
	if order.pizza != None:
		quantity = order.qty_pizza
		price = order.pizza.price
		pizza_price = price * quantity

	addition_price=0
	addition_count=0
	sub_price=0
	if order.sub != None:
		sub_price = order.sub.price
		#for the price of additions, we need to iterate to get the price of each addition
		if order.additions != None:
			additions = order.additions.all()
			for addition in additions:
				addition_price += addition.price
				addition_count += 1

	pasta_price=0
	if order.pasta != None:
		quantity = order.qty_pasta
		price = order.pasta.price
		pasta_price = price * quantity

	salad_price=0
	if order.salad != None:
		quantity = order.qty_salad
		price = order.salad.price
		salad_price = price * quantity

	dplatter_price=0
	if order.dplatter != None:
		quantity = order.qty_dplatter
		price = order.dplatter.price
		dplatter_price = price * quantity
	
	price = [{"pizza_price": pizza_price, "sub_price": sub_price, "addition_price": addition_price,
		"pasta_price": pasta_price, "salad_price": salad_price, "dplatter_price": dplatter_price}]

	total_price = pizza_price + sub_price + addition_price + pasta_price + salad_price + dplatter_price

	aprice=order.additions_price()
	print(aprice)
	print(order.additions.all())

	# following line is a test I'm doing with models and not really related to this function
	tprice = order.tot_price()

	context = {
		"order": order,
		"price": price,
		"total_price": total_price,
		"num_additions": addition_count,
		"tprice": tprice
	}


	return render(request, "orders/order.html", context)

#@login_required(login_url="login")
def checkout(request):

	order_id = request.POST["order_id"]

	order = Order.objects.get(pk=order_id)

	try:
		i=0
		additions = order.additions.all()
		for addition in additions:
			i+=1
		num_additions=i
	except:
		pass

	pizza_price=0
	if order.pizza != None:
		pizza_price = order.pizza.price

	addition_price=0
	addition_count=0
	sub_price=0
	if order.sub != None:
		sub_price = order.sub.price
		#for the price of additions, we need to iterate to get the price of each addition
		if order.additions != None:
			additions = order.additions.all()
			for addition in additions:
				addition_price += addition.price
				addition_count += 1

	pasta_price=0
	if order.pasta != None:
		pasta_price = order.pasta.price

	salad_price=0
	if order.salad != None:
		salad_price = order.salad.price

	dplatter_price=0
	if order.dplatter != None:
		dplatter_price = order.dplatter.price
	
	price = [{"pizza_price": pizza_price, "sub_price": sub_price, "addition_price": addition_price,
		"pasta_price": pasta_price, "salad_price": salad_price, "dplatter_price": dplatter_price}]

	total_price = pizza_price + sub_price + addition_price + pasta_price + salad_price + dplatter_price
	
	
	context = { 
		"order": order, 
		"total_price": total_price
	}


	return render(request, "orders/checkout.html", context)
