from django.test import TestCase
from django.utils.timezone import now
from users.models import CustomUser
from inbox.models import Message

class InboxModelTest(TestCase):
    def setUp(self):
        # Create test users
        self.sender = CustomUser.objects.create_user(username="senderuser", password="12345", email="sender@example.com")
        self.recipient = CustomUser.objects.create_user(username="recipientuser", password="12345", email="recipient@example.com")

        # Create a test message
        self.message = Message.objects.create(
            sender=self.sender,
            recipient=self.recipient,
            subject="Test Subject",
            body="This is a test message."
        )

    def test_message_creation(self):
        """Test if the message is created successfully"""
        self.assertEqual(self.message.sender.username, "senderuser")
        self.assertEqual(self.message.recipient.username, "recipientuser")
        self.assertEqual(self.message.subject, "Test Subject")
        self.assertFalse(self.message.archived)  # Ensure default archived status is False

    def test_message_str_method(self):
        """Test the string representation of the message"""
        expected_str = f"Test Subject - {self.sender} to {self.recipient}"
        self.assertEqual(str(self.message), expected_str)
