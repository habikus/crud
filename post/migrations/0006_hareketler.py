# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20170902_0508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hareketler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adsoyad', models.CharField(max_length=60, verbose_name='Adı Soyadı')),
                ('kitapadi', models.CharField(max_length=60, verbose_name='Kitap Adı')),
                ('alistarihi', models.DateTimeField(verbose_name='Alış Tarihi')),
                ('verilistarihi', models.DateTimeField(verbose_name='Veriliş Tarihi')),
                ('aciklama', models.TextField(verbose_name='Açıklama')),
                ('slug', models.SlugField(editable=False, max_length=70, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Hareketler',
            },
        ),
    ]
