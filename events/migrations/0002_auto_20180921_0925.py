# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-21 03:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='member',
            new_name='member_type',
        ),
    ]
