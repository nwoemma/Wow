from django.urls import path
from . import views

app_name = "Cart"

urlpatterns = [
    path("add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("remove/<int:cart_item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("cart_detail", views.cart_detail, name="cart_detail"),
    path('shop/', views.shop, name='shop'),
    path('shop_single/', views.shop_single, name="shop_single")
]