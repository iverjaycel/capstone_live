# Generated by Django 3.2.5 on 2022-04-13 04:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0011_alter_appointment_meeting_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='is_Done',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='meeting_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 13, 12, 24, 41, 743870)),
        ),
    ]
