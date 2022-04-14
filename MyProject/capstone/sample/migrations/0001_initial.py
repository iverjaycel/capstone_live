# Generated by Django 3.2.5 on 2022-04-11 06:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adviser',
            fields=[
                ('adviserID', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('idnum', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('available_anytime', models.IntegerField(default=0)),
                ('schedule_date', models.DateField(null=True)),
                ('schedule_time', models.TimeField(null=True)),
                ('isLoggedIn', models.BooleanField(default=False)),
                ('isDeleted', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'adviser',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.CharField(max_length=1000)),
                ('room', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='RoomMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('uid', models.CharField(max_length=200)),
                ('room_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentID', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('idnum', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('course', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('isLoggedIn', models.BooleanField(default=False)),
                ('isDeleted', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointmentID', models.AutoField(primary_key=True, serialize=False)),
                ('meeting_type', models.CharField(max_length=100)),
                ('meeting_status', models.CharField(default='pending', max_length=100)),
                ('meeting_date', models.DateField(default=datetime.datetime(2022, 4, 11, 14, 28, 42, 806263))),
                ('meeting_time', models.TimeField()),
                ('is_Approved', models.IntegerField(default=0)),
                ('meeting_counselor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Adviser', to='sample.adviser')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student', to='sample.student')),
            ],
            options={
                'db_table': 'appointment',
            },
        ),
    ]