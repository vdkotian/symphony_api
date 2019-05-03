from rest_framework import serializers
from music_api.models import TrackInformation
from music_api.models import ArtistInformation


class TrackInformationSerializer(serializers.ModelSerializer):
    """
    This is utility for mapping model into JSON format.
    """
    artist_name = serializers.ReadOnlyField(source='artistId.artistName', read_only='True')
    # trackName = serializers.CharField(max_length=120)
    class Meta:
        """Meta class to serialize the fields"""
        model = TrackInformation
        fields = ('trackName', 'artist_name', 'trackId', 'artistId', 'country', 'genreName', 'releaseDate')

    def create(self, validated_data):
        return TrackInformation.objects.create(**validated_data)


class ArtistInformationSerializer(serializers.ModelSerializer):
    """This is utility for mapping model to JSON for Artist information."""
    class Meta:
        """This is to seralize the fields"""
        model = ArtistInformation
        fields = ('artistId','artistName')

    def create(self, validated_data):
        return ArtistInformation.objects.create(**validated_data)