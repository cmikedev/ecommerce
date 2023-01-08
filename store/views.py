from django.shortcuts import render
from .models import photos, Contact


def store(request):
    photo = photos.objects.all()
    context = {'photo': photo}
    return render(request, 'store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)
