from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
import json
import datetime
from .models import *
from .forms import *


def welcome(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/welcome.html', context)


class StoreView(generic.ListView):

    """
    This class is used to create the store view
    """

    model = Product
    paginate_by = 8
    template_name = 'store/store.html'


class AddProductView(SuccessMessageMixin, generic.CreateView):
    model = Product
    form_class = NewProductForm
    template_name = 'store/add-product.html'
    success_url = reverse_lazy('storelist')
    success_message = 'New product added!'


class UpdateProductView(SuccessMessageMixin, generic.UpdateView):
    model = Product
    template_name = 'store/update-product.html'
    fields = ['title', 'manufacturer', 'description', 'licence', 'price', ]
    success_url = reverse_lazy('storelist')
    success_message = 'Product details have successfully been updated.'


class DeleteProductView(generic.DeleteView):
    model = Product
    template_name = 'store/delete-product.html'
    success_url = reverse_lazy('storelist')


class AddCommentView(SuccessMessageMixin, generic.CreateView):
    model = Comment
    template_name = 'store/add-comment.html'
    form_class = CommentForm
    success_url = reverse_lazy('storelist')
    success_message = 'Thank you. Your comment has been posted.'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.name = self.request.user.username
        return super().form_valid(form)


class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'store/detail.html'


"""
The four functions ('cart', 'checkout', 'update_item' and
'process_order') have been taken from Dennis Ivy's tutorial.
Please see README.md
"""


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
                                                     customer=customer,
                                                     complete=False
                                                    )
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, }
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
                                                     customer=customer,
                                                     complete=False
                                                    )
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def update_item(request):

    """
    This function updates the quantity count in the cart screen
    """

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
                                                 customer=customer,
                                                 complete=False
                                                )

    orderItem, created = OrderItem.objects.get_or_create(
                                                         order=order,
                                                         product=product
                                                        )

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def process_order(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
                                                     customer=customer,
                                                     complete=False
                                                    )
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
            )

    else:
        print('User is not logged in')

    return JsonResponse('Payment submitted..', safe=False)


def payment_received(request):
    return render(request, 'store/payment.html', {})
