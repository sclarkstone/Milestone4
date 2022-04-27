from django.test import TestCase
from .reviews import Review

class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        