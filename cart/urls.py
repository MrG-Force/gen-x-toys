from django.urls import path

from cart.views import add_to_cart, cart, delete_item, update_cart, checkout, checkout_billing_form, hx_menu_cart, hx_cart_total, hx_checkout_btn, hx_cart_items

urlpatterns = [
    path('add_to_cart/<str:toy_id>/', add_to_cart, name='add_to_cart'),
    path('update_cart/<str:toy_id>/<str:action>/', update_cart, name='update_cart'),
    path('cart/', cart, name='cart'),
    path('cart/checkout', checkout, name='checkout'),
    path('cart/checkout_billing_form', checkout_billing_form, name='checkout_billing_form'),
    path('delete_item/<str:toy_id>/', delete_item, name='delete_item'),
    path('hx_menu_cart/', hx_menu_cart, name='hx_menu_cart'),
    path('hx_cart_total/', hx_cart_total, name='hx_cart_total'),
    path('hx_checkout_btn/', hx_checkout_btn, name='hx_checkout_btn'),
    path('hx_cart_items/', hx_cart_items, name='hx_cart_items'),
]