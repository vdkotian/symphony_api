from django.contrib import admin
from music_api.models import TrackInformation
from music_api.models import ArtistInformation
# Register your models here.


admin.site.register(TrackInformation)
admin.site.register(ArtistInformation)