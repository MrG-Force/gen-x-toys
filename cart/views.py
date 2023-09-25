from django.shortcuts import render
from .cart import Cart
from toy.models import Toy

def add_to_cart(request, toy_id):
    cart = Cart(request)
    cart.add(toy_id)
    
    return render(request, 'cart/menu_cart.html')

def cart(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})

def update_cart(request, toy_id, action):
    cart = Cart(request)

    if action == "increase":
        cart.add(toy_id)
    else:
        cart.add(toy_id, -1)
    
    toy = Toy.objects.get(pk=toy_id)
    quantity = cart.get_item(toy_id)['quantity']

    item = {
        'toy': {
            'id': toy.id,
            'title': toy.title,
            'price': toy.price,
            'image': {
                'url': toy.image.url,
            },
        },
        'quantity': quantity,
        'total_price': toy.price * quantity,
    }
    response = render(request, 'cart/partials/cart_item.html', {'item': item})

    return response