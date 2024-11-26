from django.db import models

# Create your models here.
class Movies(models.Model):
    image=models.CharField(max_length=500,default='https://www.juliedray.com/wp-content/uploads/2022/01/sans-affiche.png')
    name=models.CharField(max_length=200)
    rating=models.FloatField()

    def __str__(self):
        return self.name
    