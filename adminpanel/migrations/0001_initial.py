# Generated by Django 3.1.5 on 2021-08-03 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uni_system_title', models.CharField(max_length=255, verbose_name='تایتل')),
                ('uni_system_link', models.URLField(max_length=300, verbose_name='لینک')),
                ('uni_system_image', models.ImageField(blank=True, default='', upload_to='uni_system_image/', verbose_name='عکس')),
            ],
            options={
                'verbose_name': 'سیستم دانشگاه',
                'verbose_name_plural': 'سیستم های دانشگاه',
            },
        ),
    ]
