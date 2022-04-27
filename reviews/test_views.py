from django.test import TestCase
from products.models import Product
from profiles.models import UserProfile
from .models import Review


class TestViews(TestCase):

    def test_get_reviews_details_page(self):
        product_id = Product.objects.create(name="Test", price=5.50)
        response = self.client.get(f'/reviews/{int(product_id.id)}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/review_detail.html')
    
   def test_get_my_reviews_page(self):
        user = 
        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/my_reviews.html')

    
  #  def test_get_add_reviews_page(self):

   # def test_get_edit_reviews_page(self):
    
    #def test_get_add_review(self):
    
    #def test_get_delete_review(self):

