from django.test import TestCase
from .models import Review
from products.models import Product
from checkout.models import Order, OrderLineItem
from decimal import Decimal


class TestModels(TestCase):

    def test_string_method(self):
        product_id = Product.objects.create(name="Test", price=5.50)
        order_number = Order.objects.create(
            full_name="Test",
            email='lennon@thebeatles.com',
            phone_number='07840039506',
            country='GB',
            town_or_city='TEST town',
            street_address1='test street')
        review = Review.objects.create(
            product_id=product_id.id,
            order_number=order_number.order_number,
            subject='test',
            review='test',
            rating=Decimal(1))

        review_id = Review.objects.get(
            product_id=product_id.id, order_number=order_number.order_number)
        expected_string = f"{review_id.product_id}"
        self.assertEqual(str(review_id), expected_string)
