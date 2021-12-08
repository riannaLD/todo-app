from flask_testing import TestCase
from application import app, db
from application.models import Tasks
from flask import url_for

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///",
            DEBUG=True, 
            WTF_CSRF_ENABLED=False

        )
        return app


    def setUp(self):
        # Will be called before every test
        db.create_all()

        task = Tasks(description="Test the application")
        db.session.add(task)
        db.session.commit()

    def tearDown(self):
        # Will be called after every test
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for("home"))
        self.assert200(response)
    def test_create_task_get(self):
        response = self.client.get(url_for("create_task"))
        self.assert200(response)
        
class TestRead(TestBase):
    
    def test_read_tasks(self):
        response = self.client.get(url_for("home"))
        self.assertIn("Test the application", str(response.data))

class TestCreate(TestBase): 

    def test_create_task(self):
        response = self.client.post(
            url_for("create_task"),
            json={"description": "Add a new task"},
            follow_redirects=True
        )
        new_task = Tasks.query.get(2)
        self.assertEqual("Add a new task", new_task.description)

    def test_create_task_redirect(self):
        response = self.client.post(
            url_for("create_task"),
            json={"description": "Add a new task"},
            follow_redirects=True
        )
        self.assertIn("Add a new task", str(response.data))
