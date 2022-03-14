# Generated by Django 4.0.3 on 2022-03-14 16:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('djangowikidata', '0005_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('address', models.TextField(default='')),
                ('birth_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
