from django.test import TestCase, Client
from django.contrib.auth.models import User
from django import setup
import os
from django.urls import get_resolver

from toy.models import Toy, Category

class CartTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')
        self.client = Client()
        self.category = Category.objects.create(name="Some Category")
        self.toy = Toy.objects.create(
            category = self.category,
            title = "Test Toy",
            price = 100,
            stock = 10,
            created_by=self.user
        )
    
    def test_add_to_cart(self):
        response = self.client.get(f"/add_to_cart/{self.toy.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(str(self.toy.id), self.client.session.get("cart"))

    def test_cart_view(self):
        self.client.get(f"/add_to_cart/{self.toy.id}/")
        response = self.client.get("/cart/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("cart", response.context)

    def test_update_cart(self):
        self.client.get(f"/add_to_cart/{self.toy.id}/")
        response = self.client.get(f"/update_cart/{self.toy.id}/increase/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(str(self.toy.id), self.client.session.get("cart"))
        self.assertEqual(self.client.session.get("cart")[str(self.toy.id)]['quantity'], 2)