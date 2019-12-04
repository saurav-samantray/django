from django.views.generic import ListView, DetailView

from django.shortcuts import render, get_object_or_404, Http404
from .models import Product



class ProductFeaturedListView(ListView):
	#queryset = Product.objects.all()
	#queryset = Product.objects.filter(title__icontains='orange',description__icontains='orange')
	template_name = "products/list.html"
	# def get_context_data(self, *args, **kwargs):
	# 	context = super(ProductListView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context
	def get_queryset(self,*args,**kwargs):
		request = self.request
		return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
	template_name = "products/detail.html"

	def get_queryset(self,*args,**kwargs):
		request = self.request
		return Product.objects.all().featured()


class ProductListView(ListView):
	queryset = Product.objects.all()
	#queryset = Product.objects.filter(title__icontains='orange',description__icontains='orange')
	template_name = "products/list.html"
	# def get_context_data(self, *args, **kwargs):
	# 	context = super(ProductListView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context

def product_list_view(request):
	queryset = Product.objects.all()
	context = {

		"object_list":queryset,
	}
	return render(request,"products/list.html",context)


class ProductDetailView(DetailView):
	#queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		return context
	def get_object(self,*args,**kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		instance = Product.objects.get_by_id(pk)
		if instance == None:
			raise Http404("Product doesn't exist")
		return instance

class ProductDetailSlugView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"
	def get_object(self,*args,**kwargs):
		request = self.request
		slug = self.kwargs.get('slug')
		instance = get_object_or_404(Product,slug=slug, active=True)
		return instance

def product_detail_view(request, pk=None, *args, **kwargs):
	#instance = Product.objects.get(pk=pk)
	instance = Product.objects.get_by_id(id=pk)
	print("Instance: ",instance)
	
	if instance is None:
		raise Http404("The product doesn't exist")
	context = {
		"object":instance,
	}
	return render(request,"products/detail.html",context)

