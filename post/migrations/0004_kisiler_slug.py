# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20170828_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='kisiler',
            name='slug',
            field=models.SlugField(default=1, editable=False, max_length=130, unique=True),
            preserve_default=False,
        ),
    ]