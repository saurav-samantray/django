from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product

class SearchProductView(ListView):
	template_name = "search/view.html"
	def get_context_data(self,*args,**kwargs):
		context = super(SearchProductView,self).get_context_data(*args,**kwargs)
		context['query'] = self.request.GET.get('q')
		return context

	def get_queryset(self, *args, **kwargs):
		request = self.request
		query = request.GET.get('q')
		if query is not None:
			#print('View: ',Product.objects.search(query))
			return  Product.objects.search(query)
		return Product.objects.featured()
		'''
		___icontains = subsctring check
		___iexact = exact string

		Both are case insensitive

		'''
