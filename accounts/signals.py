from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import CustomUser, profile


def create_profile(sender, instance, created, **kwargs):
    if created:
        print("Profile created")
        profile.objects.create(user=instance)


post_save.connect(create_profile, sender=CustomUser)


@receiver(post_delete, sender=profile)
def delete_user(sender, instance, **kwargs):
    print('user deleted')
    user = instance.user
    user.delete()
