# Generated by Django 3.2.13 on 2022-05-22 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_course_syllabus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='syllabus',
            field=models.TextField(max_length=5000),
        ),
    ]
