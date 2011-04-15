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

    def test_master_connection(self):
        import django.db
        self.assertEqual(django.db.connection.alias, 'default')

    def test_slave_connection(self):
        import replicated.routers
        replicated.routers.use_slave(True)
        replicated.routers.randomize_slave()
        connection = replicated.routers.get_slave_connection()
        self.assertEqual(connection.alias, 'slave')

    def test_slave_connection_noslave(self):
        import replicated.routers
        replicated.routers.use_slave(False)
        replicated.routers.randomize_slave()
        connection = replicated.routers.get_slave_connection()
        self.assertEqual(connection.alias, 'default')
