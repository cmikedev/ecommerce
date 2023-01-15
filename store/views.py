from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.http import JsonResponse
import json
import datetime
from .models import *
from .forms import CommentForm


def store(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
		cartItems = order['get_cart_items']

	products = Product.objects.all()
	context = {'products': products, 'cartItems': cartItems}
	return render(request, 'store/store.html', context)


class ProductDetail(generic.DetailView):
	model = Product
	template_name = 'store/detail.html'

	def get(self, request, slug, *args, **kwargs):
		queryset = Product.objects
		product = get_object_or_404(queryset, slug=slug)
		comments = product.comments.filter(approved=True).order_by("date_added")

		return render(
			request,
			"store/detail.html",
			{
				"product": product,
				"comments": comments,
				"commented": False,
				"comment_form": CommentForm()
			},
		)


	def post(self, request, slug, *args, **kwargs):
		queryset = Product.objects
		post = get_object_or_404(queryset, slug=slug)
		comments = post.comments.filter(approved=True).order_by("date_added")
		
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			comment_form.instance.name = request.user.username
			comment = comment_form.save(commit=False)
			comment.post = post
			comment.save()
		else:
			comment_form = CommentForm()
			
		return render(
			request,
			"store/detail.html",
			{
				"post": post,
				"comments": comments,
				"commented": True,
				"comment_form": comment_form,
			},
		)


def cart(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
		cartItems = order['get_cart_items']

	context = {'items': items, 'order': order, 'cartItems': cartItems}
	return render(request, 'store/cart.html', context)


def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total': 0, 'get_cart_items': 0 , 'shipping': False}
		cartItems = order['get_cart_items']

	context = {'items': items, 'order': order, 'cartItems': cartItems}
	return render(request, 'store/checkout.html', context)


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)


def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		total = float(data['form']['total'])
		order.transaction_id = transaction_id

		if total == order.get_cart_total:
			order.complete = True
		order.save()

		"""if order.shipping == True:
			ShippingAddress.objects.create(
			customer=customer,
			order=order,
			address=data['shipping']['address'],
			city=data['shipping']['city'],
			state=data['shipping']['state'],
			zipcode=data['shipping']['zipcode'],
			country=data['shipping']['zipcode'],
			)"""
		
		ShippingAddress.objects.create(
			customer=customer,
			order=order,
			address=data['shipping']['address'],
			city=data['shipping']['city'],
			state=data['shipping']['state'],
			zipcode=data['shipping']['zipcode'],
			)
		#------------------ Custom Code
		"""Sale.objects.create(
			#order_id=order.transaction_id,
			customer=customer,
			order=order,
			#product=product,
			#total=total,
			#created=created,
			address=data['shipping']['address'],
			city=data['shipping']['city'],
			state=data['shipping']['state'],
			zipcode=data['shipping']['zipcode'],
			)"""
		
	else:
		print('User is not logged in')

	return JsonResponse('Payment submitted..', safe=False)


def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)
