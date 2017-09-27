# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('nacionalidad', models.CharField(choices=[('USA', 'Estadounidense'), ('MX', 'Mexicana'), ('ES', 'Español'), ('FR', 'Frances'), ('IN', 'Ingles')], max_length=50)),
                ('biography', models.TextField()),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=50)),
                ('age', models.IntegerField()),
                ('is_alive', models.BooleanField(default=True)),
            ],
        ),
    ]
