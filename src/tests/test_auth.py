import unittest
from main import create_app, db


class TestAuth(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()

        db.create_all()

        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db-custom", "seed"])


    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()


    def test_main(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertIn('T2A2-B', str(response.data))
        self.assertEqual(response.status_code, 200)


    def test_sign_up(self):
        response = self.client.get('/signup', data={
            'username': 'new_user1',
            'email': 'new_user1@domain.com',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)


    def test_login(self):
        response = self.client.get('/signup', data={
            'username': 'new_user2',
            'email': 'new_user2@domain.com',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/login', data={
            'username': 'new_user2',
            'password': 'password'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_login_invalid(self):
        response = self.client.get('/signup', data={
            'username': 'new_user3',
            'email': 'new_user3@domain.com',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/login', data={
            'username': 'new_user3',
            'password': 'incorrect_password'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_log_out(self):
        response = self.client.get('/signup', data={
            'username': 'new_user4',
            'email': 'new_user4@domain.com',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/login', data={
            'username': 'new_user4',
            'password': 'password'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 302)
