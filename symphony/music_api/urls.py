from django.urls import path, include, re_path
from .views import TrackInformationView
from .views import ArtistInformationView
from .views import ArtistInformationQuerySet
from .views import ArtistTrackInfoDateFilter

app_name = "music_api"

urlpatterns = [
    re_path('^track/', TrackInformationView.as_view(), name='songs-all'), # List all songs GET
    re_path('^track/(?P<releaseDate>.+)/(?P<artistId>.+)/$', ArtistTrackInfoDateFilter.as_view(), name='datefilter-all'),# Date Filter GET
    re_path('track/(?P<artistId>[0-9]+)/', TrackInformationView.as_view(), name='track-update'), # Updates the track PUT reuqest
    path('artist/', ArtistInformationView.as_view(), name='artist-all'), # List all artists GET
    re_path('^artist/(?P<artistId>.+)/$', ArtistInformationQuerySet.as_view(), name='artist-specific'), # GET artist specific
    re_path('^artist/$/', ArtistInformationView.as_view()), #Delete artist DELETE
]

