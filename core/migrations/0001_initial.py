# Generated by Django 3.1.5 on 2021-08-09 08:40

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('professor_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateField(max_length=50, verbose_name='تاریخ رویداد')),
                ('time_left', models.DateField(auto_now_add=True, verbose_name='روز باقی مانده(تغییر ندهید)')),
                ('title', models.CharField(max_length=100, verbose_name='موضوع')),
                ('draft', models.BooleanField(default=True, verbose_name='پخش شود؟')),
            ],
            options={
                'verbose_name': 'رویداد',
                'verbose_name_plural': 'رویداد ها',
                'ordering': ('-event_date',),
            },
        ),
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_style', models.CharField(choices=[('اخبار', 'اخبار'), ('اطلاعیه', 'اطلاعیه')], default='اخبار', max_length=50, verbose_name='نوع پست')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='تاریِخ')),
                ('post_image', models.ImageField(blank=True, default='', null=True, upload_to='post_images/', verbose_name='عکس')),
                ('title', models.CharField(max_length=50, verbose_name='موضوع')),
                ('content', ckeditor.fields.RichTextField(verbose_name='متن')),
                ('draft', models.BooleanField(default=True, help_text='اگر تیک شود قابل مشاهده برای همه خواهد بود', verbose_name='پخش شود؟')),
                ('target_dep', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='professor_app.departmant', verbose_name='دپارتمانت')),
                ('written_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'خبر',
                'verbose_name_plural': 'اخبار / اطلاعیه ها',
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_type', models.CharField(choices=[('آموزش', 'آموزش'), ('همایش', 'همایش')], default='آموزش', max_length=50, verbose_name='نوع آموزش')),
                ('title', models.CharField(max_length=50, verbose_name='موضوع')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='تاریِخ')),
                ('post_image', models.ImageField(blank=True, default='', null=True, upload_to='post_images/', verbose_name='عکس')),
                ('content', ckeditor.fields.RichTextField(verbose_name='متن')),
                ('draft', models.BooleanField(default=True, help_text='اگر تیک شود قابل مشاهده برای همهخواهد بود', verbose_name='پخش شود؟')),
                ('written_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'آموزش',
                'verbose_name_plural': 'آموزش ها / همایش ها',
                'ordering': ('-date_created',),
            },
        ),
    ]
