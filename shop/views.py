from django.shortcuts import render, get_object_or_404

from . models import Category, Product

# list all products or filter products by a given category
def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	context = {
		'category': category,
		'categories': categories,
		'products': products
	}
	return render(request, 'shop/product/list.html', context)

def product_detail(request, id, slug):
	# *arg being id. slug and available being **kwargs)
	# we can get the instance just with id. slug is included to build SEO-friendly URLs for products
	# try-except would be the alternative approach to get_object_or_404
	print(slug)
	product = get_object_or_404(Product, id=id, slug=slug, available=True)
	print(product)

	# retrieving product with id only
	#product = products.objects.filter(id)

	context = {'product': product}
	return render(request, 'shop/product/detail.html', context)