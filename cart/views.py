from django.shortcuts import render
from django.http import HttpResponse
from .cart import Cart
from toy.models import Toy


def add_to_cart(request, toy_id):
    cart = Cart(request)
    cart.add(toy_id)

    return render(request, 'cart/menu_cart.html')


def cart(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})


def update_cart(request, toy_id, action=None):
    cart = Cart(request)

    if action == "increase":
        cart.add(toy_id)
    elif action == "decrease":
        cart.add(toy_id, -1)

    toy = Toy.objects.get(pk=toy_id)
    quantity = cart.get_item(toy_id)['quantity']

    item = {
        'toy': {
            'id': toy.id,
            'title': toy.title,
            'price': toy.price,
            'stock': toy.stock,
            'image': {
                'url': toy.get_image_url(),
            },
        },
        'quantity': quantity,
        'total_price': toy.price * quantity,
    }

    response = render(request, 'cart/partials/cart_item.html', {'item': item})

    response['HX-Trigger'] = 'update-menu-cart'

    return response


def delete_item(request, toy_id):
    cart = Cart(request)
    cart.remove(toy_id)

    response = HttpResponse()

    response['HX-Trigger'] = 'delete-item'

    return response


def hx_menu_cart(request):
    return render(request, 'cart/menu_cart.html')


def hx_cart_total(request):
    return render(request, 'cart/partials/cart_total.html')


def hx_checkout_btn(request):
    return render(request, 'cart/partials/checkout_btn.html')

def hx_cart_items(request):
    cart = Cart(request)
    return render(request, 'cart/partials/cart_items.html', {'cart': cart})