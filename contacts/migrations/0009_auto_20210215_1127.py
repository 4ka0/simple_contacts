# Generated by Django 3.1.6 on 2021-02-15 02:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_auto_20210215_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_modified_on',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2021, 2, 15, 2, 27, 40, 949665, tzinfo=utc)),
        ),
    ]