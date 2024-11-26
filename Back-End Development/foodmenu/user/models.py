from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_image/profile_img.jpg', upload_to='profile_image')
    location = models.CharField(max_length=500)

    def __str__(self):
        return self.user.username
    
