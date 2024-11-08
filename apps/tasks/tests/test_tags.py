from django.test import TestCase
from django.test import TestCase
from rest_framework.response import Response


class TagsTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertContains(response, "Welcome to my site!")


class TagsListTestCase(TestCase):
    def test_get_tags(self):
        response = self.client.get('/api/tags/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, Response)
        self.assertIsInstance(response.data, list)
        for tag in response.data:
            self.assertIsInstance(tag, dict)
            self.assertIn('name', tag)
            self.assertIsInstance(tag['name'], str)
            self.assertRegex(tag['name'], r'^[a-zA-z ]{4,20}$')
