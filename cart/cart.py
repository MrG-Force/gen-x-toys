from django.conf import settings
from decimal import Decimal

from toy.models import Toy

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart
    
    def __iter__(self):
        for toy_id, cart_item in self.cart.items():
            toy = Toy.objects.get(pk=toy_id)
            cart_item["toy"] = {
                'title': toy.title,
                'price': str(toy.price),
                'stock': toy.stock,
                'image': {
                    'url': toy.get_image_url(),
                }
            }
            cart_item['total_price'] = str(toy.price * cart_item['quantity'])

        return iter(self.cart.values())

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, toy_id, quantity=1):
        toy = Toy.objects.get(pk=toy_id)

        if toy_id not in self.cart:
            self.cart[toy_id] = {'quantity': 1, 'id': toy_id, 'total_price': str(toy.price)}

        else:
            self.cart[toy_id]['quantity'] += quantity
            self.cart[toy_id]['total_price'] = str(toy.price * self.cart[toy_id]['quantity'])

            if self.cart[toy_id]['quantity'] == 0:
                self.remove(toy_id)

        self.save()
    
    def remove(self, toy_id):
        if str(toy_id) in self.cart:
            self.cart.pop(str(toy_id))
            self.save()

    def get_total(self):
        return sum(Decimal(item['total_price']) for item in self.cart.values())
    
    def get_item(self, toy_id):
        toy_id = str(toy_id)
        if toy_id in self.cart:
            return self.cart[str(toy_id)]
        else:
            return None
