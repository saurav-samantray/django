from django.shortcuts import render, redirect

from products.models import Product
from .models import Cart



def cart_home(request):
	cart_obj,new_obj = Cart.objects.new_or_get(request)
	cart_id = cart_obj.id

	subtotal = cart_obj.subtotal

	print(f'GET_CART:  cartId={cart_id} , subTotal={subtotal} ')

	print("Session Key : ",request.session.session_key)
	return render(request, "carts/home.html", {})

def cart_update(request):
	product_id = 1
	product_obj = Product.objects.get(id=product_id)
	cart_obj,new_obj = Cart.objects.new_or_get(request)
	cart_obj.products.add(product_obj)
	#cart_obj.products.remove(product_obj)
	#return redirect(product_obj.get_absolute_url())
	return redirect("cart:home")
