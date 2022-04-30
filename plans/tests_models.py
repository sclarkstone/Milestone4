from django.test import TestCase
from .models import Session, Distance


class TestModels(TestCase):

    def test_session_string_method(self):
        distance = Distance.objects.create(
            name="Test",
            friendly_name='test',
            duration=6,
            product_id=1,
            instructions='test'
        )
        session = Session.objects.create(
            distance=distance,
            effort='test',
            description='test',
            week=1,
            day=1
        )
        expected_string = f"{session.effort}"
        self.assertEqual(str(session), expected_string)

    def test_distance_string_method(self):
        distance = Distance.objects.create(
            name="Test",
            friendly_name='test',
            duration=6,
            product_id=1,
            instructions='test'
        )
        expected_string = f"{distance.name}"
        self.assertEqual(str(distance), expected_string)
