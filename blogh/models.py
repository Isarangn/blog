from django.db import models

from django.utils import timezone
# To set author i.e. user from User Table we need to add below import
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    # need author having relation with Users table in Django Database
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return self.title

    def get_absolute_url(self): #After creating post redirect to post-detail page
        return reverse('post-detail', kwargs={'pk':self.pk})


'''
class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=35)
    mobile = models.IntegerField(max_length=13)
    msg = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    


    def __str__(self):
        return self.name
'''