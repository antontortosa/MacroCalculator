# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 22:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='histories',
            old_name='id_item',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='histories',
            old_name='id_usuario',
            new_name='usuario',
        ),
        migrations.RenameField(
            model_name='ingredients',
            old_name='id_item',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='objectives',
            old_name='id_usuario',
            new_name='usuario',
        ),
    ]
