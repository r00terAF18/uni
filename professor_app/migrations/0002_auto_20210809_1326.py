# Generated by Django 3.1.5 on 2021-08-09 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('professor_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='p_user',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
