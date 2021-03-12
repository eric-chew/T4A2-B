import unittest
from main import create_app, db


class TestFeedbacks(unittest.TestCase):
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

    def test_feedback_show(self):
        response = self.client.get('/feedback/1', follow_redirects=True)
        self.assertIn('Acceptable', str(response.data))
        self.assertEqual(response.status_code, 200)

    def test_feedback_show_project(self):
        response = self.client.get(
            '/feedback/project/1',
            follow_redirects=True
        )
        self.assertIn('user3', str(response.data))
        self.assertIn('user4', str(response.data))
        self.assertEqual(response.status_code, 200)
