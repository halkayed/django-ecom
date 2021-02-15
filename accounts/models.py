from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return str(self.address)

@receiver(post_save, sender=User)
def create_profile(sender, instance ,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)