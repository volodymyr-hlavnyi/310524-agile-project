import json
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from apps.users.models import User

from apps.users.choices.positions import UserPositions


class UserAPITests(APITestCase):

    def setUp(self):
        self.user_list_url = reverse('user-list')
        self.register_user_url = reverse('user-register')

    def test_get_all_users(self):
        # Создаем тестовых пользователей
        User.objects.create(username='user1', first_name='John', last_name='Doe', email='john@example.com',
                            position=UserPositions.PROGRAMMER.value)
        User.objects.create(username='user2', first_name='Jane', last_name='Doe', email='jane@example.com',
                            position=UserPositions.PROJECT_MANAGER.value)

        response = self.client.get(self.user_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_register_new_user(self):
        user_data = {
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'newuser@example.com',
            'position': UserPositions.QA.value,
            'password': 'StrongPassword123',
            're_password': 'StrongPassword123'
        }

        response = self.client.post(self.register_user_url, data=json.dumps(user_data), content_type='application/json')
        # print(response.content)  # Add this line to print the response content
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'newuser')

    def test_get_user_detail(self):
        user = User.objects.create(
            username='user1',
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            position=UserPositions.PROGRAMMER.value
        )
        url = reverse('user-detail', args=[user.id])
        response = self.client.get(url)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'user1')
        self.assertEqual(response.data['first_name'], 'John')
        self.assertEqual(response.data['last_name'], 'Doe')
        self.assertEqual(response.data['email'], 'john@example.com')
        self.assertEqual(response.data['position'], UserPositions.PROGRAMMER.value)

    def test_user_detail_fields(self):
        user = User.objects.create(
            username='user1',
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            position=UserPositions.PROGRAMMER.value
        )
        url = reverse('user-detail', args=[user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('username', response.data)
        self.assertIn('first_name', response.data)
        self.assertIn('last_name', response.data)
        self.assertIn('email', response.data)
        self.assertIn('position', response.data)
        self.assertIsInstance(response.data['username'], str)
        self.assertIsInstance(response.data['first_name'], str)
        self.assertIsInstance(response.data['last_name'], str)
        self.assertIsInstance(response.data['email'], str)
        self.assertIsInstance(response.data['position'], str)

    def test_get_user_detail_non_existent(self):
        url = reverse('user-detail', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
