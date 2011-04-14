from django.test import TestCase

class TestMasterSlave(TestCase):

    def test_get_request(self):
        response = self.client.get('/test_request')
        self.assertEqual(response.content, 'slave')

    def test_post_request(self):
        response = self.client.post('/test_request')
        self.assertEqual(response.content, 'default')

    def test_get_use_slave(self):
        response = self.client.get('/test_use_slave')
        self.assertEqual(response.content, 'slave')

    def test_post_use_slave(self):
        response = self.client.post('/test_use_slave')
        self.assertEqual(response.content, 'slave')

    def test_get_use_master(self):
        response = self.client.get('/test_use_master')
        self.assertEqual(response.content, 'default')

    def test_post_use_master(self):
        response = self.client.post('/test_use_master')
        self.assertEqual(response.content, 'default')
