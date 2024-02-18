from django.db import models
from twitterapp.models import UserProfile
from profileapp.models import Profiles

class Dweet(models.Model):
    user = models.ForeignKey('twitterapp.UserProfile', on_delete=models.CASCADE, related_name='dweet')
    body = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField('profileapp.Profiles', blank=True, related_name='like')
    def __str__(self):
        return self.body[:30]
    
    class Meta:
        ordering = ['-modified', '-created']