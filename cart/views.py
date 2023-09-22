from django.shortcuts import render
from .cart import Cart

def add_to_cart(request, toy_id):
    cart = Cart(request)
    cart.add(toy_id)
    
    return render(request, 'cart/menu_cart.html')
