from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import Doner

# for creating a new user with the 'customer' group

@receiver(post_save, sender=User)
def customer_profile(sender, instance, created, **kwargs):
    if created:
        
        group, created = Group.objects.get_or_create(name='Donor')

        
        instance.groups.add(group)

        # Create a Customer profile for the user
        Doner.objects.create(
            user=instance,
            name=instance.username,
        )
        print("Profile created!")
