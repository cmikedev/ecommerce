from django.urls import path, include, re_path
from . import views


urlpatterns = [
    #path('', views.store, name='store'),
    #path('', views.StoreView.as_view(), name='store'),
    path('', views.welcome, name='store'),
    path('store', views.StoreView.as_view(), name='storelist'),
    #path('add-product', views.product_create, name='product_create'),
    path('add-product/', views.AddProductView.as_view(), name='product_create'),
    path('detail/<slug:slug>/<int:pk>/', views.ProductDetail.as_view(), name='detail'),
    path('detail/<slug:slug>/<int:pk>/comment/', views.AddCommentView.as_view(), name='comment_add'),
    path('detail/update/<slug:slug>/<int:pk>/', views.UpdateProductView.as_view(), name='product_update'),
    path('detail/<slug:slug>/<int:pk>/delete', views.DeleteProductView.as_view(), name='product_delete'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('contact/', views.contact, name='contact'),
]