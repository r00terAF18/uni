# Generated by Django 3.1.5 on 2021-08-10 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sidebar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sidebar_title', models.CharField(max_length=255, verbose_name='تایتل')),
                ('sidebar_on_page', models.CharField(choices=[('Daneshkadeh', 'دانشکده'), ('Ostad', 'استاد'), ('Lecture', 'آموزش'), ('News', 'اخبار')], help_text='صفحه ای که سایدبار نشان داده شود', max_length=15, verbose_name='صفحه')),
                ('sidebar_is_active', models.BooleanField(default=True, verbose_name='سایدبار فعال باشد؟')),
            ],
            options={
                'verbose_name': 'سایدبار',
                'verbose_name_plural': 'سایدبار ها',
            },
        ),
        migrations.CreateModel(
            name='SidebarItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sidebar_item_title', models.CharField(max_length=255, verbose_name='تایتل')),
                ('sidebar_link', models.SlugField(allow_unicode=True, verbose_name='لینک')),
                ('sidebar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sidebar_app.sidebar')),
            ],
        ),
    ]
