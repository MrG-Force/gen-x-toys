from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import BillingForm, PaymentForm, ShippingForm
from .cart import Cart
from toy.models import Toy


def add_to_cart(request, toy_id):
    cart = Cart(request)
    cart.add(toy_id)

    return render(request, 'cart/menu_cart.html')


def cart(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', { 'cart': cart })


def update_cart(request, toy_id, action=None):
    cart = Cart(request)

    if action == "increase":
        cart.add(toy_id)
    elif action == "decrease":
        cart.add(toy_id, -1)

    toy = Toy.objects.get(pk=toy_id)
    quantity = cart.get_item(toy_id)['quantity']

    cart_item = {
        'toy': {
            'title': toy.title,
            'price': toy.price,
            'stock': toy.stock,
            'image': {
                'url': toy.get_image_url(),
            },
        },
        'quantity': quantity,
        'id': toy_id,
        'total_price': toy.price * quantity,
    }

    response = render(request, 'cart/partials/cart_item.html', { 'item': cart_item })

    response['HX-Trigger'] = 'update-menu-cart'

    return response


def delete_item(request, toy_id):
    cart = Cart(request)
    cart.remove(toy_id)

    response = HttpResponse()

    response['HX-Trigger'] = 'delete-item'

    return response

def checkout(request):
    billingForm = BillingForm()
    shippingForm = ShippingForm()
    paymentForm = PaymentForm()
    cart = Cart(request)
            
    return render(request, 'cart/checkout.html', { 'cart': cart, 'billingForm': billingForm, 'shippingForm': shippingForm, 'paymentForm': paymentForm })

def checkout_billing_form(request):
    billingForm = BillingForm()
    shippingForm = ShippingForm()
    paymentForm = PaymentForm()
    cart = Cart(request)

    if request.method == 'POST':
        print("Received POST request")
        billingForm = BillingForm(request.POST)
        if billingForm.is_valid():
            billingFormComplete = True
            request.session['billingForm'] = billingForm.cleaned_data
            print("Cleaned data: ", request.session['billingForm'])
            response = render(request, 'cart/checkout.html', { 'cart': cart, 'billingForm': billingForm, 'shippingForm': shippingForm, 'paymentForm': paymentForm, 'billingFormComplete': billingFormComplete })
            return response

            
    return render(request, 'cart/checkout.html', { 'cart': cart, 'billingForm': billingForm, 'shippingForm': shippingForm, 'paymentForm': paymentForm })


def hx_menu_cart(request):
    return render(request, 'cart/menu_cart.html')


def hx_cart_total(request):
    return render(request, 'cart/partials/cart_total.html')


def hx_checkout_btn(request):
    return render(request, 'cart/partials/checkout_btn.html')


def hx_cart_items(request):
    cart = Cart(request)
    return render(request, 'cart/partials/cart_items.html', {'cart': cart})