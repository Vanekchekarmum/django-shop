# Generated by Django 3.2.9 on 2021-12-02 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oursite', '0006_auto_20211202_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='created',
        ),
        migrations.RemoveField(
            model_name='video',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='video',
            name='title',
        ),
        migrations.RemoveField(
            model_name='video',
            name='updated',
        ),
    ]
