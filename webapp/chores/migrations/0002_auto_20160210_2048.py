# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chore',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]