from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import TrackInformation
from .models import ArtistInformation
from symphony.serializer import TrackInformationSerializer
from symphony.serializer import ArtistInformationSerializer


class ArtistTrackInfoDateFilter(generics.ListAPIView):
    """This class handels the GET request for date and artist filter"""
    # TODO: Try to integrate with TrackInformationViews
    serializer_class = TrackInformationSerializer

    def get_queryset(self):
        """This method is called with the URL for tracks is passed with ArtistId and Release date."""
        artistId = self.kwargs.get('artistId')
        releaseDate = self.kwargs.get('releaseDate')
        queryset = TrackInformation.objects.all()
        da = datetime.strptime(releaseDate, '%d-%m-%Y')
        filter_query = queryset.filter(artistId__artistId=artistId, releaseDate__lte=da)
        return filter_query


class ArtistInformationQuerySet(generics.ListAPIView):
    """This class is specifically designed to handel GET request for artist ID. For E.G if there is Request for artistID
    then this view class will be called."""
    serializer_class = TrackInformationSerializer

    def get_queryset(request):
        artist_id = request.kwargs.get('artistId')
        if not artist_id:
            return Response({"response": 'FAIL', 'message': 'Please specify artistID'})
        try:
            artist_obj = ArtistInformation.objects.get(artistId=artist_id)
        except ArtistInformation.DoesNotExist:
            return []
        track_queryset = TrackInformation.objects.filter(artistId=artist_obj)
        return track_queryset


class ArtistInformationView(APIView):
    """ This view is for handling operation for Artist Information. It will perform GET, POST, DELETE request
    for artist information."""

    def get(self, pk=None):
        """Performs GET operation. Returns a Response with all artist information"""
        """This will handel all the GET request."""
        track_info = ArtistInformation.objects.all()
        serializer = ArtistInformationSerializer(track_info, many=True)
        return Response({"artist_info": serializer.data})

    def post(self, request):
        """Performs POST operation. Creates new artist record.  Returns a Response with artist information"""

        artist_name = request.data.get('name')
        serializer = ArtistInformationSerializer(data={'artistName': artist_name})
        if serializer.is_valid(raise_exception=True):
            artist_save = serializer.save()
        return Response({"response": 'SUCCESS', 'artistId': '{}'.format(artist_save.artistId),
                         "message": "Artist'{}' created successfully".format(artist_save.artistName)})

    def delete(self, request):
        """Performs DELETE operation. Deleted the artisrt ID record from the DB.
        Returns a Response with all artist information"""
        artistId = request.data.get('artistId')
        try:
            del_obj = ArtistInformation.objects.get(artistId=artistId)
            del_obj.delete()
            return Response({'response': 'SUCCESS', 'message': "Artist '{}' Deleted Successfully".format(artistId)})
        except ArtistInformation.DoesNotExist:
            return Response({'response': 'FAIL'})


class TrackInformationView(APIView):
    """This class handels the GET, POST, PUT operations for Tracks"""

    def check_track_exsist(self, **kwargs):
        """This is a custom method for retriving trackId and artistId"""
        try:
            artist_obj = TrackInformation.objects.get(trackId=kwargs.get('trackId')[0], artistId__artistId=kwargs.get('artistId')[0])
        except TrackInformation.DoesNotExist:
            artist_obj = []
        return artist_obj

    def get(self, request):
        track_info = TrackInformation.objects.all()
        serializer = TrackInformationSerializer(track_info, many=True)
        return Response({"track_info": serializer.data})

    def post(self, request):
        track_info = request.data.copy()
        track_info['releaseDate'] = datetime.datetime.now()
        serializer = TrackInformationSerializer(data=track_info, many=True)
        if serializer.is_valid(raise_exception=True):
            track_save = serializer.save()
        return Response({"response": 'SUCCESS', 'trackId': '{}'.format(track_save.artistId),
                         "message": "Track'{}' created successfully".format(track_save.trackName)})

    def put(self, request):
        """This method handels the Updates on Track Information"""
        da = request.data.copy()
        obj_data = self.check_track_exsist(**da)
        print(da)
        if not self.check_track_exsist(**da):
            return Response({'response': 'FAIL', 'message': 'Please check TrackID/ArtistID'})
        serializer = TrackInformationSerializer(obj_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)