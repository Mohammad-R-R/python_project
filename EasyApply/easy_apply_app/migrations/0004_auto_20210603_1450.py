# Generated by Django 2.2.4 on 2021-06-03 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easy_apply_app', '0003_auto_20210603_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='specialist',
            field=models.CharField(choices=[('', ''), ('Engineering', 'Engineering'), ('Doctor', 'Doctor'), ('Pharmacy', 'Pharmacy'), ('IT', 'IT'), ('Science', 'Science'), ('Math', 'Math'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology'), ('Phisycs', 'Phisycs'), ('Sport', 'Sport'), ('Finance', 'Finance'), ('Managment', 'Managment')], default='', max_length=255),
        ),
    ]
