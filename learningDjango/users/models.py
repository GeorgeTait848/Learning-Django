from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')

    def __str__(self) -> str:
        return '{} Profile'.format(self.user.username)

    def save(self):
        '''overriding the save method to resize image if it is too big'''
        
        super().save()
        img = Image.open(self.image.path)

        #check if this image is more than 300px in height or width

        if img.height > 300 or img.width > 300:
            outputSz = (300, 300)
            img.thumbnail(outputSz) # resize image
            img.save(self.image.path)
