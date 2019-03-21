# Generated by Django 2.1.7 on 2019-03-21 02:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceshi1', '0009_imgmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadmodel',
            name='file',
            field=models.FileField(upload_to='file/%Y%m%d', validators=[django.core.validators.FileExtensionValidator(['txt', 'pdf'])]),
        ),
    ]
