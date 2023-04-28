from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Annoucement

class IdeaTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
            department="Computer Science and Mathematics",
            program="Computer Science",
            user_id="19010301043",
            full_name="Test User",
            is_staff=False,
            is_doctor=False
        )

        cls.announce = Annoucement.objects.create(
            author = cls.user,
            title = "A good title",
            body="Nice body content",
        )

    def test_announcement_model(self):
        self.assertEqual(self.announce.author.username, "testuser")
        self.assertEqual(self.announce.title, "A good title")
        self.assertEqual(self.announce.body, "Nice body content")
        self.assertEqual(str(self.announce), "A good title")