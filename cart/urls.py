from django.urls import path

from cart.views import add_to_cart, cart, update_cart

urlpatterns = [
    path('add_to_cart/<int:toy_id>/', add_to_cart, name='add_to_cart'),
    path('update_cart/<int:toy_id>/<str:action>/', update_cart, name='update_cart'),
    path('cart/', cart, name='cart'),
]