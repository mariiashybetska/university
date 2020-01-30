from django.test import TestCase, Client
import unittest


class TestStudentsList(unittest.TestCase):
    def test_details(self):
        client = Client()
        response = client.get('/students/list/')
        self.assertEqual(response.status_code, 200)




