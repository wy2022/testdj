# Generated by Django 2.1.7 on 2019-03-21 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceshi1', '0006_auto_20190321_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadmodel',
            name='img',
            field=models.ImageField(default=1, upload_to='file/img/%Y%m%d'),
            preserve_default=False,
        ),
    ]