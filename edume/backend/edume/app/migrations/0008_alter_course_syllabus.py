# Generated by Django 3.2.13 on 2022-05-22 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_chapter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='syllabus',
            field=models.TextField(default='', max_length=5000),
        ),
    ]