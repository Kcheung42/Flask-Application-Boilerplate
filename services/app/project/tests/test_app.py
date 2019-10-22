import json
import unittest
from project.tests.base import BaseTestCase


class TestAppService(BaseTestCase):

    def test_app(self):
        """Ensure the /ping route behaves correctly."""

        response = self.client.get('/app/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

if __name__ == '__main__':
    unittest.main()
