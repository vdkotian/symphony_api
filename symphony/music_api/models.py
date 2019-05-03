from django.db import models
# Create your models here.

"""There could have been two models Artist and TrackInformation which would have been better off as 
it would be easy to handel relations"""


class ArtistInformation(models.Model):
    artistId = models.AutoField(primary_key=True)
    artistName = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return '{}-{}'.format(self.artistId, self.artistName)

    class Meta:
        ordering = ['artistName']


class TrackInformation(models.Model):
    trackId = models.AutoField(primary_key=True)
    trackName = models.CharField(max_length=100, null=True, blank=True)
    artistId = models.ForeignKey(ArtistInformation, on_delete=models.CASCADE)
    country = models.CharField(max_length=3, null=True, blank=True)
    genreName = models.CharField(max_length=50, null=True, blank=True)
    releaseDate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '{}-{}-{}'.format(self.trackId, self.trackName, self.genreName)

    class Meta:
        ordering = ['trackName']