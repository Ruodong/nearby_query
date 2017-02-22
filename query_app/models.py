from django.db import models

# Create your models here.

class Place(models.Model):
    placeid = models.TextField()
    formatted_address = models.TextField()
    vicinity_address = models.TextField()
    location_lat = models.FloatField()
    location_lng = models.FloatField()
    icon = models.URLField()
    name = models.TextField()
    phone_number = models.TextField()
    rating = models.FloatField()
    permanently_closed = models.BooleanField()
    url = models.URLField()
    website = models.URLField()

    def __str__(self):
        return self.name
