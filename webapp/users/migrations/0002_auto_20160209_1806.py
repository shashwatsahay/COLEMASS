# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 17:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='is_usable',
            new_name='is_broken',
        ),
    ]