from django.db import models
from dweetapp.models import Dweet
from profileapp.models import Profiles
from twitterapp.models import UserProfile

class Comment(models.Model):
    user = models.ForeignKey('twitterapp.UserProfile',null=True, blank=True, on_delete=models.CASCADE, related_name='comment_like')
    dweet = models.ForeignKey('dweetapp.Dweet', on_delete=models.CASCADE, related_name='comment')
    body = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    like_comment = models.ManyToManyField('profileapp.Profiles', blank=True, related_name='comment_like')

    def __str__(self):
        return self.body[:30]
    
    class Meta:
        ordering = ['-created']