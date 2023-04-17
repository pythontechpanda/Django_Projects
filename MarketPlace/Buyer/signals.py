from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User
from Supplier.models import FollowersCount

@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    if created:
        FollowersCount.objects.create(user=instance)