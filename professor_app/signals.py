from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from .models import Professor
from django.dispatch import receiver


@receiver(pre_save, sender=Professor)
def create_user(sender, instance, **kwargs):
    print(f'\nHERE SOME DATA -> ')
    print(instance)
    print(f'<- HERE SOME DATA \n ')
    # u = User.objects.create(first_name=instance)
    # p = Professor.objects.get(instance)
