from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Category, Toy

class CategoryModelTest(TestCase):
    def test_string_representation(self):
        category = Category(name="Some Category")
        self.assertEqual(str(category), "Some Category")

class ToyModelTest(TestCase):
    def setUp(self):
        # Create a User
        self.user = User.objects.create(username='testuser', password='12345')
        
        # Create a Category
        self.category = Category.objects.create(name='Action Figures')
        
        
    def test_string_representation(self):
        toy = Toy(title="Toy One", category=self.category, price=10.99, stock=5)
        self.assertEqual(str(toy), "Toy One")

    def test_field_types(self):
        toy = Toy.objects.create(
            title="Toy Two", category=self.category, price=10.99, stock=5, created_by=self.user
        )
        self.assertIsInstance(toy.category, Category)
        self.assertIsInstance(toy.title, str)
        self.assertIsInstance(toy.price, float)
        self.assertIsInstance(toy.stock, int)

        toy.delete()
        
    def test_object_creation(self):
        toy = Toy.objects.create(
            title="Toy Three", category=self.category, price=10.99, stock=5, created_by=self.user
        )
        self.assertEqual(Toy.objects.count(), 1)
        toy.delete()

class ToyDetailViewTests(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')

        self.category = Category.objects.create(name='Action Figures')

        self.toy1 = Toy.objects.create(title="Toy1", category=self.category, price=10.99, stock=5, created_by=self.user)
        self.toy2 = Toy.objects.create(title="Toy2", category=self.category, price=12.99, stock=5, created_by=self.user)
        self.toy3 = Toy.objects.create(title="Toy3", category=self.category, price=14.99, stock=0, created_by=self.user)
        self.toy4 = Toy.objects.create(title="Toy4", category=self.category, price=15.99, stock=6, created_by=self.user)
        self.toy5 = Toy.objects.create(title="Toy5", category=self.category, price=16.99, stock=7, created_by=self.user)

    def test_get_valid_toy(self):
        response = self.client.get(reverse('toy:detail', args=[self.toy1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['toy'], self.toy1)

    def test_get_invalid_toy(self):
        response = self.client.get(reverse('toy:detail', args=[9999]))
        self.assertEqual(response.status_code, 404)

    def test_related_toys(self):
        response = self.client.get(reverse('toy:detail', args=[self.toy1.pk]))
        self.assertQuerysetEqual(
            response.context['related_toys'],
            [self.toy5, self.toy4, self.toy2],
            ordered=False
        )

    def test_template_used(self):
        response = self.client.get(reverse('toy:detail', args=[self.toy1.pk]))
        self.assertTemplateUsed(response, 'toy/detail.html')
