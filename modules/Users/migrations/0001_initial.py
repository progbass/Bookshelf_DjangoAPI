# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('id', models.AutoField(primary_key=True, unique=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('apaterno', models.CharField(max_length=40)),
                ('amaterno', models.CharField(max_length=40)),
                ('numero_celular', models.CharField(max_length=10, unique=True, null=True)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('genero', models.CharField(max_length=16, blank=True, choices=[('M', 'Mujer'), ('H', 'Hombre')])),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(verbose_name='groups', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
