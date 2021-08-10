from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from .models import Professor
from django.dispatch import receiver


@receiver(pre_save, sender=Professor)
def check_data(sender, instance, **kwargs):
    username = instance.f_name + " " + instance.l_name
    u = User.objects.create(
        username=username,
        first_name=instance.f_name,
        last_name=instance.l_name,
        email=instance.email,
        is_superuser=True,
    )
    u.set_password(instance.password)
    u.save()
    instance.p_user = u
