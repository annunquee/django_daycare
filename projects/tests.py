from django.test import TestCase
from django.contrib.auth import get_user_model
from projects.models import Project

User = get_user_model()

class ProjectModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="12345")

        # Create a test project (update 'owner' → 'user')
        self.project = Project.objects.create(
            user=self.user,  # FIXED: Change 'owner' to 'user'
            title="Test Project",
            description="This is a test project",
            stakeholders="Client A",
            status="Pending",
        )

    def test_project_creation(self):
        """Test if the project is created successfully"""
        self.assertEqual(self.project.title, "Test Project")
        self.assertEqual(self.project.user.username, "testuser")  # FIXED: Change 'owner' to 'user'

    def test_project_str_method(self):
        """Test the string representation of the project"""
        self.assertEqual(str(self.project), "Test Project")
