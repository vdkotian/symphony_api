from django.test import TestCase
# Create your tests here.
from .models import TrackInformation
from .models import ArtistInformation
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from datetime import datetime
import pytz


class ModelTestCase(TestCase):
    """This class is for testing the models"""

    def setUp(self):
        """Define the test variables and other resources"""
        self.artistId = "1234"
        self.artistName = 'VdKotian'
        self.artist_information = ArtistInformation(artistName=self.artistName)

    def test_trackinfomation_create(self):
        """This will test if it can be   created or not"""
        old_count = ArtistInformation.objects.count()
        self.artist_information.save()
        updated_count = ArtistInformation.objects.count()
        self.assertNotEqual(old_count, updated_count)


class TrackInformationTestCase(TestCase):
    """This class has all the mthodes and functionality to Test"""

    def setUp(self):

        """Defining the variables and other resouces here"""
        self.trackName = "Test Track"
        self.country = "USA"
        self.genreName = "Test Genre"
        self.releaseDate = datetime.now(tz=pytz.timezone('Asia/Kolkata'))
        self.artist_obj = ArtistInformation.objects.create(artistName="Test Artist")
        self.track_info_obj = TrackInformation(trackName=self.trackName, artistId=self.artist_obj,
                                               genreName=self.genreName, releaseDate=self.releaseDate,
                                               country=self.country)

    def test_artistinformation(self):
        old_count = TrackInformation.objects.count()
        self.track_info_obj.save()
        updated_count = TrackInformation.objects.count()
        self.assertNotEqual(old_count, updated_count)
