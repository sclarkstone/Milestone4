from django.test import TestCase
from django.test import Client
from products.models import Product
from django.contrib.auth.models import User
from checkout.models import Order, OrderLineItem
from profiles.models import UserProfile
from .models import Session, Distance


class TestViews(TestCase):

    def test_get_plan_details_page(self):
        self.client = Client()
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        product_id = Product.objects.create(name="Test", price=5.50)
        user_profile = UserProfile.objects.get(user=self.user)
        order_number = Order.objects.create(user_profile=user_profile ,full_name="john", email='lennon@thebeatles.com', phone_number='07840039506', country='GB', town_or_city='TEST town', street_address1='test street')
        order_item = OrderLineItem.objects.create(order=order_number, product=product_id)

        response = self.client.get(f'/plans/{int(product_id.id)}/')
        print((f'/plans/{int(product_id.id)}/'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'plans/plan_detail.html')
    
    def test_get_my_plans_page(self):
        self.client = Client()
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/plans/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'plans/my_plans.html')


