from django.test import TestCase, Client
from django.urls import reverse
from django.core.management import call_command

from django.core import mail

import unittest
from faker import Faker


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


class TestStudents(TestCase):
    fake = Faker()
    # fixtures = ['db.json']

    @classmethod
    def setUpClass(cls):
        call_command('loaddata', 'db.json', verbosity=0)


    def setUp(self) -> None:
        print('Setup')

    def tearDown(self) -> None:
        print('teardown')

    def _gen_data(self):
        return {
            'subject': self.fake.word(),
            'text': self.fake.text(),
        }

    def test_contact_form(self):
        data = {
            'email': self.fake.email(),
            **self._gen_data(),
        }
        response = self.client.post(reverse('contact'), data=data)
        assert response.status_code == 302

    def test_contact_form_wrong_email(self):
        data = {
            'email': 'wrong_email',
            **self._gen_data(),
        }
        response = self.client.post(reverse('contact'), data=data)
        assert response.status_code == 200

    def test_contact_form_empty_subject(self):
        data = {
            'email': self.fake.email(),
            'subject': '',
            'text': self.fake.text(),
        }
        response = self.client.post(reverse('contact'), data=data)
        assert response.status_code == 200







