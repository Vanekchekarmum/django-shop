# Generated by Django 3.2.9 on 2021-12-08 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oursite', '0023_video_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]