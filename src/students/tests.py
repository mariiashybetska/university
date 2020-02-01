from django.test import TestCase, Client
from django.urls import reverse
import unittest


class TestStudentsList(unittest.TestCase):
    def test_details(self):
        client = Client()
        response = client.get(reverse('students'))
        self.assertEqual(response.status_code, 200)


class TestContact(TestCase):

    def test_contact_is_valid(self):
        data = {
            'email': 'mshybetskaya@gmail.com',
            'subject': 'hhjdjdfh',
            'message': 'hydhyys'
        }
        response = self.client.post(reverse('contact'), data)
        assert response.status_code == 200

        data['email'] = 'WRONG'
        response = self.client.post(reverse('contact'), data)
        assert response.status_code in (301, 302)
        #self.ssertEqual(response.status_code == 302)







