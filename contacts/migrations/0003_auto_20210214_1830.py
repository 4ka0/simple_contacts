# Generated by Django 3.1.6 on 2021-02-14 09:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20210212_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='last_modified_on',
            field=models.DateField(verbose_name=datetime.datetime(2021, 2, 14, 9, 30, 4, 115407, tzinfo=utc)),
        ),
    ]
