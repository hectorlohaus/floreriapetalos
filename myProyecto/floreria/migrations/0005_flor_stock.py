# Generated by Django 3.0 on 2019-12-10 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floreria', '0004_auto_20191210_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='flor',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
