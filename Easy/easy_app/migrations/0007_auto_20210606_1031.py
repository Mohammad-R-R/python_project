# Generated by Django 2.2.4 on 2021-06-06 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easy_app', '0006_auto_20210604_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='driving',
            field=models.BooleanField(default=False),
        ),
    ]
