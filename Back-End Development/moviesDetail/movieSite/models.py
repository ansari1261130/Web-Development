from django.db import models

# Create your models here.
class MovieData(models.Model):
    image=models.ImageField(upload_to='images/',default='images/coming_soon.jpg')
    name=models.CharField(max_length=200)
    duration=models.FloatField()
    rating=models.FloatField()
    genre=models.CharField(max_length=200,default='action')

    def __str__(self):
        return self.name