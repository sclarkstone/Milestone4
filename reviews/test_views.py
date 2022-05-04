from django.test import TestCase
from django.test import Client
from products.models import Product
from django.contrib.auth.models import User
from checkout.models import Order, OrderLineItem
from django.shortcuts import reverse
from .forms import UserReviewForm
from decimal import Decimal

from .models import Review


class TestViews(TestCase):

    def test_get_reviews_details_page(self):
        product_id = Product.objects.create(name="Test", price=5.50)
        response = self.client.get(f'/reviews/{int(product_id.id)}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/review_detail.html')

    def test_get_my_reviews_page(self):
        self.client = Client()
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/my_reviews.html')

    def test_get_add_review_page(self):
        self.client = Client()
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        product_id = Product.objects.create(name="Test", price=5.50)
        order_number = Order.objects.create(
            full_name="Test",
            email='samclarkstone@hotmail.com',
            phone_number='07840039506',
            country='GB',
            town_or_city='TEST town',
            street_address1='test street')
        response = self.client.get(
            f'/reviews/add/{int(product_id.id)}/{str(order_number)}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/add_review.html')

    def test_get_edit_review_page(self):
        self.client = Client()
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        product_id = Product.objects.create(name="Test", price=5.50)
        order_number = Order.objects.create(
            full_name="Test",
            email='lennon@thebeatles.com',
            phone_number='07840039506',
            country='GB',
            town_or_city='TEST town',
            street_address1='test street')
        response = self.client.get(
            f'/reviews/edit/{int(product_id.id)}/{str(order_number)}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/edit_review.html')

    def test_can_edit_review(self):
        self.client = Client()
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        product_id = Product.objects.create(name="Test", price=5.50)
        order_number = Order.objects.create(
            full_name="Test",
            email='samclarkstone@hotmail.com',
            phone_number='07840039506',
            country='GB',
            town_or_city='TEST town',
            street_address1='test street')
        response = self.client.post(
            f'/reviews/edit/{int(product_id.id)}/{str(order_number)}',
            {
                'subject': 'test',
                'review': 'test',
                'rating': '5.00'
            })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/edit_review.html')

    def test_can_add_review(self):
        self.client = Client()
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        product_id = Product.objects.create(name="Test", price=5.50)
        order_number = Order.objects.create(
            full_name="Test",
            email='lennon@thebeatles.com',
            phone_number='07840039506',
            country='GB',
            town_or_city='TEST town',
            street_address1='test street')
        response = self.client.post(
            f'/reviews/add/{int(product_id.id)}/{str(order_number)}',
            {
                'subject': 'test',
                'review': 'test',
                'product_id': product_id.id,
                'order_number': order_number.order_number,
                'rating': 1.0
            })
        self.assertRedirects(response, '/reviews/')

    def test_can_delete_review(self):
        self.client = Client()
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        product_id = Product.objects.create(name="Test", price=5.50)
        order_number = Order.objects.create(
            full_name="Test",
            email='lennon@thebeatles.com',
            phone_number='07840039506',
            country='GB',
            town_or_city='TEST town',
            street_address1='test street')
        review_id = Review.objects.create(
            product_id=product_id.id,
            order_number=order_number.order_number,
            subject='test',
            review='test',
            rating=1.0)
        response = self.client.get(
            f'/reviews/delete/{int(review_id.product_id)}/{str(review_id.order_number)}'
        )
        self.assertRedirects(response, '/reviews/')
        existing_items = Review.objects.filter(
            product_id=review_id.product_id,
            order_number=review_id.order_number)
        self.assertEqual(len(existing_items), 0)
