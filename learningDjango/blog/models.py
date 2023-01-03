from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model): 
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # now is a function however we dont want to execute it, only pass the function as an argument

    # possible options: 
    # auto_now = True - upates to current datetime any time a modification is made to the post.
    #auto_now_add = True - sets to time created and does not defer from this time, however can never update when the class instance was created.

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
