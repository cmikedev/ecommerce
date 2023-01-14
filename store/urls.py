from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.store, name='store'),
    path('detail/<slug:slug>/', views.ProductDetail.as_view(), name='detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('contact/', views.contact, name='contact'),
]
