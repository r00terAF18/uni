# Generated by Django 3.1.5 on 2021-08-12 07:57

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("faculty_app", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Lecture",
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
                ("title", models.CharField(max_length=50, verbose_name="موضوع")),
                (
                    "date_created",
                    django_jalali.db.models.jDateTimeField(
                        auto_now_add=True, verbose_name="تاریِخ"
                    ),
                ),
                (
                    "post_image",
                    models.ImageField(
                        blank=True,
                        default="",
                        null=True,
                        upload_to="post_images/",
                        verbose_name="عکس",
                    ),
                ),
                ("content", ckeditor.fields.RichTextField(verbose_name="متن")),
                (
                    "draft",
                    models.BooleanField(
                        default=True,
                        help_text="اگر تیک شود قابل مشاهده برای همهخواهد بود",
                        verbose_name="پخش شود؟",
                    ),
                ),
                (
                    "target_dep",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="faculty_app.departmant",
                        verbose_name="دانشکده",
                    ),
                ),
                (
                    "written_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "آموزش",
                "verbose_name_plural": "آموزش ها",
                "ordering": ("-date_created",),
            },
        ),
    ]
