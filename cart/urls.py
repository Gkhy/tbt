from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("add_cart/<int:product_pk>/", views.add_cart, name="add_cart"),
    path("", views.cart_detail, name="cart_detail"),
]
