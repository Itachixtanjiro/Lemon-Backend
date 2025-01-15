from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test Menu instances
        self.item1 = Menu.objects.create(title="Pizza", price=150, inventory=50)
        self.item2 = Menu.objects.create(title="Pasta", price=120, inventory=30)
        self.client = APIClient()

    def test_get_all(self):
        # Get all menu items
        response = self.client.get('/restaurant/menu/')
        # Serialize the data
        serialized_items = MenuSerializer([self.item1, self.item2], many=True)
        # Assert the response status and data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized_items.data)
