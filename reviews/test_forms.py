from django.test import TestCase
from .forms import UserReviewForm


class TestItemForm(TestCase):

    def test_item_subject_is_required(self):
        form = UserReviewForm({'subject': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('subject', form.errors.keys())
        self.assertEqual(form.errors['subject'][0], 'This field is required.')
    
    def test_item_review_is_required(self):
        form = UserReviewForm({'review': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('review', form.errors.keys())
        self.assertEqual(form.errors['review'][0], 'This field is required.')
    
    def test_item_rating_is_required(self):
        form = UserReviewForm({'rating': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors.keys())
        self.assertEqual(form.errors['rating'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = UserReviewForm()
        self.assertEqual(form.Meta.fields, ['subject', 'review', 'rating'])
