# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20170828_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitaplar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kitapadi', models.CharField(max_length=30, verbose_name='Kitap Adı')),
                ('yazari', models.CharField(max_length=30, verbose_name='Yazarı')),
                ('yayinevi', models.CharField(max_length=30, verbose_name='Yayinevi')),
                ('turu', models.CharField(max_length=30, verbose_name='Türü')),
                ('aciklama', models.TextField(verbose_name='Açıklama')),
            ],
        ),
        migrations.RenameModel(
            old_name='Post',
            new_name='Kisiler',
        ),
    ]
