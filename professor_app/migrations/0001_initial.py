# Generated by Django 3.1.5 on 2021-08-03 19:24

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Departmant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='دپارتمانت')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='departmant/', verbose_name='عکس')),
                ('info', ckeditor.fields.RichTextField(verbose_name='پیام رئیس دانشکده')),
            ],
            options={
                'verbose_name': 'دانشکده',
                'verbose_name_plural': 'دانشکده ها',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=255, verbose_name='نام')),
                ('l_name', models.CharField(max_length=255, verbose_name='نام خانوادگی')),
                ('email', models.EmailField(max_length=255, verbose_name='ایمیل')),
                ('image', models.ImageField(blank=True, default='', upload_to='staff/', verbose_name='عکس')),
                ('level_of_education', models.CharField(max_length=50, verbose_name='مرتبه علمی')),
                ('phone_number', models.CharField(blank=True, max_length=15, verbose_name='شماره داخلی')),
                ('p_user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'استاد',
                'verbose_name_plural': 'اساتید',
            },
        ),
        migrations.CreateModel(
            name='ProfessorUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_about', ckeditor.fields.RichTextField(blank=True, verbose_name='توضیحات')),
                ('p_education', ckeditor.fields.RichTextField(blank=True, verbose_name='سوابق تحصیلی')),
                ('p_liking', ckeditor.fields.RichTextField(blank=True, verbose_name='زمینه های تحقیقاتی مورد علاقه')),
                ('p_papers_isi', ckeditor.fields.RichTextField(blank=True, verbose_name='مقالات چاپ شده در نشریات معتبر علمی- پژوهشی بین المللی و ISI')),
                ('p_papers', ckeditor.fields.RichTextField(blank=True, verbose_name='مقالات چاپ شده در نشریات معتبر داخلی')),
                ('p_convention_isi', ckeditor.fields.RichTextField(blank=True, verbose_name='همایش های بین المللی')),
                ('p_convention', ckeditor.fields.RichTextField(blank=True, verbose_name='همایش های ملی و منطقه ای')),
                ('p_translation', ckeditor.fields.RichTextField(blank=True, verbose_name='تالیف و ترجمه کتاب')),
                ('p_projects_pending', ckeditor.fields.RichTextField(blank=True, verbose_name='طرح های تحقیقاتی در دست اجرا')),
                ('p_projects_complete', ckeditor.fields.RichTextField(blank=True, verbose_name='طرح های تحقیقاتی خاتمه یافته')),
                ('p_education_project', ckeditor.fields.RichTextField(blank=True, verbose_name='راهنمایی و مشاوره پروژه های کارشناسی، پایان نامه های کارشناسی ارشد و رساله های دکتری')),
                ('p_projects', ckeditor.fields.RichTextField(blank=True, verbose_name='فعالیتهای اجرایی')),
                ('p_prizes', ckeditor.fields.RichTextField(blank=True, verbose_name='جوایز و افتخارات')),
                ('p_professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professor_app.professor')),
            ],
            options={
                'verbose_name': 'درباره استاد',
                'verbose_name_plural': 'درباره اساتید',
            },
        ),
        migrations.CreateModel(
            name='ProfessorPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='تایتل پست')),
                ('image', models.ImageField(blank=True, null=True, upload_to='professor_post/', verbose_name='عکس')),
                ('content', ckeditor.fields.RichTextField(verbose_name='متن')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professor_app.professor')),
            ],
            options={
                'verbose_name': 'پست استاد',
                'verbose_name_plural': 'پست اساتید',
            },
        ),
        migrations.CreateModel(
            name='DepLab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام')),
                ('lab_link', models.CharField(max_length=255, verbose_name='لینک')),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professor_app.departmant')),
            ],
            options={
                'verbose_name': 'دانشکده آزمایشگاه',
                'verbose_name_plural': 'دانشکده آزمایشگاه ها',
            },
        ),
        migrations.CreateModel(
            name='DepForms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام')),
                ('form_file', models.FileField(upload_to='department/forms/', verbose_name='فورم')),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professor_app.departmant')),
            ],
            options={
                'verbose_name': 'فایل دانشکده',
                'verbose_name_plural': 'فایل های دانشکذه',
            },
        ),
        migrations.AddField(
            model_name='departmant',
            name='head',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='head', to='professor_app.professor', verbose_name='رئیس دانشکده'),
        ),
        migrations.AddField(
            model_name='departmant',
            name='ostads',
            field=models.ManyToManyField(related_name='ostads', to='professor_app.Professor', verbose_name='Ostadan'),
        ),
    ]
