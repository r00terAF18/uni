from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Professor


@receiver(pre_save, sender=Professor)
def check_data(sender, instance, **kwargs):
    if hasattr(instance, "p_user"):
        instance.p_user.delete()
    username = instance.f_name + " " + instance.l_name
    new_u = User.objects.create(
        username=username,
        first_name=instance.f_name,
        last_name=instance.l_name,
        email=instance.email,
        is_staff=True,
        is_superuser=True
    )
    new_u.set_password(instance.password)
    new_u.save()
    instance.p_user = new_u
    
