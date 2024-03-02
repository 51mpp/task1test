import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_true_when_X_is_17(self):
        response = self.app.get('/is_prime/17')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'],True)

    def test_false_when_X_is_36(self):
        response = self.app.get('/is_prime/36')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'],False)

    def test_true_when_X_is_13219(self):
        response = self.app.get('/is_prime/13219')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'],True)
