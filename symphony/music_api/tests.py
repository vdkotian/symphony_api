from django.test import TestCase
# Create your tests here.
from .models import TrackInformation
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
# Create your views here.


class ViewTestCase(TestCase):
    """Test suite for API views."""

    def setUp(self):
        """Setting up test variables"""
        self.client = APIClient()
        self.track_information_data = {'artistId': '1234', 'artistName': 'VdKotian'}
        self.response = self.client.post(reverse('create'), self.track_information_data, format="json")

    def test_trackinformation_create(self):
        """This will check if the track information can be created"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


class ModelTestCase(TestCase):
    """This class is for testing the models"""

    def setUp(self):
        """Define the test variables and other resources"""
        self.artistId = "1234"
        self.artistName = 'VdKotian'
        self.trackinformation_obj = TrackInformation(artistName=self.artistName, artistId=self.artistId)

    def test_trackinfomation_create(self):
        """This will test if it can be   created or not"""
        old_count = TrackInformation.objects.count()
        self.trackinformation_obj.save()
        updated_count = TrackInformation.objects.count()
        self.assertNotEqual(old_count, updated_count)
