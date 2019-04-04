"""Unit tests module."""

from django.test import TestCase
from django.test import Client

from cars.models import Car


class CarTest(TestCase):
    """Test cars app."""

    def setUp(self):
        """Add new record to db."""
        Car.objects.create(
            id="d8bdab33-490f-4f24-8510-5ab220e44de5",
            model="Prius",
            producent="Toyota",
            passangers=5,
            production_year=2009,
            electric_or_hybrid=True,
            category="5d",
            registration_number="SK9959"
            )

    def test_list(self):
        """Test for method list."""
        data = {
            'data': [
                {
                    'category': 'No info',
                    'electric_or_hybrid': 'No info',
                    'id': 'd8bdab33-490f-4f24-8510-5ab220e44de5',
                    'model': 'Prius',
                    'passangers': 5,
                    'producent': 'Toyota',
                    'production_year': 2009,
                    'registration_number': 'SK9959'
                }
            ]
        }
        c = Client()
        response = c.get('/cars/list')
        self.assertEqual(response.json(), data)

    def test_retrive(self):
        """Test for method retrieve."""
        data = {
            'data':
                {
                    'category': 'No info',
                    'electric_or_hybrid': 'No info',
                    'id': 'd8bdab33-490f-4f24-8510-5ab220e44de5',
                    'model': 'Prius',
                    'passangers': 5,
                    'producent': 'Toyota',
                    'production_year': 2009,
                    'registration_number': 'SK9959'
                }
        }
        c = Client()
        response = c.get('/cars/retrive?id=d8bdab33-490f-4f24-8510-5ab220e44de5')
        self.assertEqual(response.json(), data)

    def test_create(self):
        """Test for method create."""
        c = Client()
        data = {
            "model": "Prius",
            "producent": "Toyota",
            "passangers": 5,
            "production_year": 2009,
            "electric_or_hybrid": True,
            "category": "5d",
            "registration_number": "SK9959"
        }

        response = c.post('/cars/create', data)

        self.assertEqual(response.status_code, 200)

    def test_update(self):
        """Test for method update."""
        data = {
            "model": "Corolla"
        }

        c = Client()
        response = c.put('/cars/update?id=d8bdab33-490f-4f24-8510-5ab220e44de5', data)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        """Test for method delete."""
        success = {
            "status": "204",
            "message": "Car has been deleted."
        }

        c = Client()
        response = c.delete('/cars/delete?id=d8bdab33-490f-4f24-8510-5ab220e44de5')
        self.assertEqual(response.json(), success)
