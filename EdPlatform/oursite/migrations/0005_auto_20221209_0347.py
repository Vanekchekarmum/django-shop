# Generated by Django 3.2.9 on 2022-12-08 22:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('oursite', '0004_auto_20221209_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constructor',
            name='slug',
            field=models.SlugField(default=uuid.UUID('5669c365-774a-11ed-b355-5c80b6f716a0'), max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(default=uuid.UUID('56692730-774a-11ed-b3cb-5c80b6f716a0'), max_length=200),
        ),
        migrations.AlterField(
            model_name='module',
            name='slug',
            field=models.SlugField(default=uuid.UUID('56694e31-774a-11ed-9379-5c80b6f716a0'), max_length=200),
        ),
    ]
