# Generated by Django 2.2.4 on 2021-06-04 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easy_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
