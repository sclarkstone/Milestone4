from django.test import TestCase

class TestViews(TestCase):

    def test_get_reviews_details_page(self):
        response = self.client.get('/reviews/7/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/review_detail.html')
    
 #   def test_get_reviews_page(self):
    
  #  def test_get_add_reviews_page(self):

   # def test_get_edit_reviews_page(self):
    
    #def test_get_add_review(self):
    
    #def test_get_delete_review(self):

