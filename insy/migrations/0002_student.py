# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-14 03:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('CE', 'Civil Engineering'), ('CHE', 'Chemical Engineering'), ('CSE', 'Computer Science & Engineering'), ('ECE', 'Electronics & Commmunication Engineering'), ('EEE', 'Electrical & Electronics Engineering'), ('ME', 'Mechanical Engineering'), ('PE', 'Production Engineering')], default='CSE', max_length=100)),
                ('semester', models.CharField(choices=[('S1', 'Semester I'), ('S2', 'Semester II'), ('S3', 'Semester III'), ('S4', 'Semester IV'), ('S5', 'Semester V'), ('S6', 'Semester VI'), ('S7', 'Semester VII'), ('S8', 'Semester VIII')], default=1, max_length=50)),
                ('date_of_registration', models.DateField()),
                ('name', models.CharField(max_length=30)),
                ('university_roll_no', models.CharField(max_length=20)),
                ('name_of_parent', models.CharField(max_length=30)),
                ('address', models.TextField(max_length=100)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]