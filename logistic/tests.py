from rest_framework.test import APIClient, APITestCase


class TestApiView(APITestCase):
    def test_sample_view(self):
        client = APIClient()
        response = client.get('/test/')
        self.assertEqual(response.status_code, 200)
