import unittest
from app import app


class TestHandleFormSubmission(unittest.TestCase):

    def setUp(self):
        # Create a Flask test client
        self.client = app.test_client()

        # Disable Flask's error handling during tests
        app.testing = True

    def test_handle_form_submission(self):
        # Simulate a POST request with form data
        response = self.client.post('/', data={'input_text': 'Hello'})

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the response contains the expected reversed text
        expected_reversed_text = 'olleH'
        self.assertIn(expected_reversed_text, response.get_data(as_text=True))

        # Add more assertions if needed

if __name__ == '__main__':
    unittest.main()
