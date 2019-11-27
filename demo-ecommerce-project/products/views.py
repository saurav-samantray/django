from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    print("DEBUG: all products display")
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})