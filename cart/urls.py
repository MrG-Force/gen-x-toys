from django.urls import path

from cart.views import add_to_cart, cart, delete_item, update_cart, hx_menu_cart, hx_cart_total, hx_checkout_btn, hx_cart_items, show_confirmation, hx_hide_confirmation

urlpatterns = [
    path('add_to_cart/<int:toy_id>/', add_to_cart, name='add_to_cart'),
    path('update_cart/<int:toy_id>/<str:action>/', update_cart, name='update_cart'),
    path('cart/', cart, name='cart'),
    path('delete_item/<int:toy_id>/', delete_item, name='delete_item'),
    path('show_confirmation/<int:toy_id>/', show_confirmation, name='show_confirmation'),
    path('hx_menu_cart/', hx_menu_cart, name='hx_menu_cart'),
    path('hx_cart_total/', hx_cart_total, name='hx_cart_total'),
    path('hx_checkout_btn/', hx_checkout_btn, name='hx_checkout_btn'),
    path('hx_cart_items/', hx_cart_items, name='hx_cart_items'),
    path('hx_hide_confirmation/<int:toy_id>/', hx_hide_confirmation, name='hx_hide_confirmation')
]