# Generated by Django 3.0 on 2019-12-10 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flor',
            fields=[
                ('nombre', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('valor', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField()),
                ('fotografia', models.ImageField(null=True, upload_to='pelis')),
            ],
        ),
    ]
