from django.contrib.auth.models import User
from django.db import models

class Order(models.Model):
    CREATED = 'created'
    ORDERED = 'ordered'
    SHIPPED = 'shipped'
    CANCELLED = 'cancelled'
    DELIVERED = 'delivered'

    STATUS_CHOICES = [
        (CREATED, 'Created'),
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped'),
        (CANCELLED, 'Cancelled'),
        (DELIVERED, 'Delivered'),
    ]
    user = models.ForeignKey(User, related_name='orders', blank=True, null=True, on_delete=models.CASCADE)
    billing_details = models.ForeignKey('BillingDetails', related_name='orders', blank=True, null=True, on_delete=models.PROTECT)
    shipping_details = models.ForeignKey('ShippingDetails', related_name='orders', blank=True, null=True, on_delete=models.PROTECT)
    payment = models.ForeignKey('Payment', related_name='orders', blank=True, null=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=CREATED)
    paid = models.BooleanField(default=False)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

class BillingDetails(models.Model):
    user = models.ForeignKey(User, related_name='billing_details', blank=True, null=True, on_delete=models.CASCADE)
    address = models.OneToOneField('Address', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

class ShippingDetails(models.Model):
    user = models.ForeignKey(User, related_name='shipping_details', blank=True, null=True, on_delete=models.CASCADE)
    address = models.OneToOneField('Address', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Address(models.Model):
    STATES_CHOICES = [
        ('NSW', 'New South Wales'),
        ('VIC', 'Victoria'),
        ('QLD', 'Queensland'),
        ('SA', 'South Australia'),
        ('WA', 'Western Australia'),
        ('TAS', 'Tasmania'),
        ('ACT', 'Australian Capital Territory'),
        ('NT', 'Northern Territory'),
    ]

    street_address = models.CharField(max_length=200)
    apartment_address = models.CharField(max_length=20)
    suburb = models.CharField(max_length=100)
    state = models.CharField(max_length=3, choices=STATES_CHOICES)
    postal_code = models.CharField(max_length=12)

class Payment(models.Model):
    user = models.ForeignKey(User, related_name='payments', blank=True, null=True, on_delete=models.CASCADE)
    # fields related to the payment method, might include a token from a payment provider
    # but avoid storing sensitive details directly

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    toy = models.ForeignKey('toy.Toy', related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)