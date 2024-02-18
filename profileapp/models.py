from django.db import models
from twitterapp.models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=UserProfile)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profiles(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profiles)
        user_profile.save()

class Profiles(models.Model):
    user = models.OneToOneField('twitterapp.UserProfile', on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        'self',
        related_name='following',
        symmetrical=False,
        blank=True
    )
    friend_request = models.ManyToManyField(
        'self',
        related_name='requested_by',
        symmetrical=False,
        blank=True
    )
    place = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username