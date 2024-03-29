# Generated by Django 3.2.9 on 2022-12-08 22:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20221209_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default=uuid.UUID('566aae3d-774a-11ed-9042-5c80b6f716a0'), max_length=250),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(default=uuid.UUID('566aae3f-774a-11ed-851a-5c80b6f716a0'), max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(default=uuid.UUID('566aae3e-774a-11ed-9056-5c80b6f716a0'), max_length=20),
        ),
    ]
