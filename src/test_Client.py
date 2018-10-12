import unittest
from Client import Client


class TestOop1MajorClient(unittest.TestCase):
    def setUp(self):
        self.client_data = \
            ('Carrie Cordon',
             'carrie.cordon@gmail.com',
             '404-444-1111',
             'VISA',
             'PAID',
             'Doesn\'t pay on time',
             'Give notice to pay.')

        self.client = Client(self.client_data)

    def test_add_credits(self):
        self.assertEqual(0, self.client.credits)
        self.client.add_credits(5)
        self.assertEqual(5, self.client.credits)
