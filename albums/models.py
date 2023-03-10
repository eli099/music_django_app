from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.title} - {self.artist} ({self.year})"