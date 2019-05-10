from django.test import TestCase, Client
from bs4 import BeautifulSoup
# Create your tests here.
class TestView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 2001)

        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.title

        print(title)



