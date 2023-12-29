from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.userprofile = UserProfile.objects.create(user=self.user, interests='sports, music')

    def test_user_profile_creation(self):
        user_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(user_profile.interests, 'sports, music')