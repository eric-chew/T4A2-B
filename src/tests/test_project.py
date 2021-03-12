import unittest
from main import create_app, db


class TestProjects(unittest.TestCase):
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

    def test_project_index(self):
        response = self.client.get('/projects', follow_redirects=True)
        self.assertIn('Projects', str(response.data))
        self.assertEqual(response.status_code, 200)

    def test_project_show(self):
        response = self.client.get('/projects/1', follow_redirects=True)
        self.assertIn('google', str(response.data))
        self.assertEqual(response.status_code, 200)
