import unittest
from flask import Flask
from app import app  # Importeer de Flask-app vanuit je applicatiebestand


class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_app_runs(self):
        response = self.app.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
