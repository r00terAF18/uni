# Generated by Django 3.1.5 on 2021-08-12 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Carousel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "carousel_title",
                    models.CharField(
                        default="سلایدر", max_length=100, verbose_name="نام سلایدر"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="اگر تیک شود قابل مشاهده برای همه خواهد بود",
                        verbose_name="فعال شود؟",
                    ),
                ),
            ],
            options={
                "verbose_name": "سلایدر",
                "verbose_name_plural": "سلایدر ها",
            },
        ),
        migrations.CreateModel(
            name="CarouselItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "img",
                    models.ImageField(
                        blank=True,
                        default="",
                        null=True,
                        upload_to="carousel/",
                        verbose_name="عکس",
                    ),
                ),
                (
                    "details",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="متن"
                    ),
                ),
                (
                    "item_carousel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="slider_app.carousel",
                    ),
                ),
            ],
            options={
                "verbose_name": "سلایدر",
                "verbose_name_plural": "سلایدر ها",
            },
        ),
    ]
