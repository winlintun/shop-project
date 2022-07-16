from django.shortcuts import render
from .models import Products, Category
from random import shuffle
# Create your views here.



def home(request):
	products = Products.objects.all()
	context = {
		'products': products,
	}
	return render(request, 'products/index.html', context)


def item_detail(request, item_id):
	products = Products.objects.get(pk=item_id)
	some_products = Products.objects.all().order_by('-date')[:4]
	context = {
		'products': products,
		'some_products': some_products,
	}
	return render(request, 'products/shop-item.html', context)