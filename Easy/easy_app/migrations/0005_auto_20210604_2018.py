# Generated by Django 2.2.4 on 2021-06-04 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easy_app', '0004_auto_20210604_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(blank=True, unique=True),
        ),
    ]