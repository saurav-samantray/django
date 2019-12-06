from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed

from products.models import Product
User = settings.AUTH_USER_MODEL

# Create your models here.

VALID_UPDATE_ACTION = ['post_add','post_remove','post_clear']


class CartManager(models.Manager):
	def new_or_get(self,request):
		cart_id = request.session.get("cart_id",None)
		qs = self.get_queryset().filter(id=cart_id)
		if qs.count() == 1:
			new_obj = False
			print(f'Cart Id exists {cart_id} ')
			cart_obj = qs.first()
			if request.user.is_authenticated() and cart_obj.user is None:
				print(f'User is authenticated associating {cart_id} with {user}')
				cart_obj.user = request.user
				cart_obj.save()
		else:
			new_obj = True
			cart_obj = self.new(user=request.user)
			request.session['cart_id'] = cart_obj.id
			print('Cart Id not found in DB. Created new cart : ',cart_obj.id)
		return cart_obj,new_obj

	def new(self,user=None):
		user_obj = None
		if user is not None:
			if user.is_authenticated():
				user_obj = user
		return self.model.objects.create(user=user_obj)


class Cart(models.Model):
	user		= models.ForeignKey(User, null=True, blank=True)
	products 	= models.ManyToManyField(Product, blank=True)
	subtotal		= models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
	total		= models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
	updated		= models.DateTimeField(auto_now=True)
	timestamp	= models.DateTimeField(auto_now_add=True)

	objects 	= CartManager()
	def __str__(self):
		return str(self.id)



def m2m_changed_cart_receiver(sender,instance, action, *args,**kwargs):	
	if action in VALID_UPDATE_ACTION:
		products = instance.products.all()
		total = 0
		for product in products:
			total += product.price
		if instance.subtotal != total:
			instance.subtotal = total
			instance.save()

m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)


def pre_save_cart_receiver(sender,instance, *args,**kwargs):	
	instance.total = instance.subtotal + 10

pre_save.connect(pre_save_cart_receiver, sender=Cart)
