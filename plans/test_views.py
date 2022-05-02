from django.test import TestCase
from django.test import Client
from products.models import Product
from django.contrib.auth.models import User
from checkout.models import Order, OrderLineItem
from profiles.models import UserProfile
from .models import Session, Distance


class TestViews(TestCase):

    def test_get_my_plans_page(self):
        self.client = Client()
        self.user = User.objects.create_user(
            'john',
            'lennon@thebeatles.com',
            'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/plans/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'plans/my_plans.html')
