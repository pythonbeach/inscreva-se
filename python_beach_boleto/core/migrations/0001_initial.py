# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Nome', max_length=50)),
                ('email', models.EmailField(verbose_name='Email', max_length=254, unique=True)),
                ('degree', models.CharField(verbose_name='Formação', max_length=100)),
                ('state', models.CharField(verbose_name='Estado', choices=[('PI', 'Piauí'), ('CE', 'Ceará'), ('MA', 'Maranhão')], max_length=30)),
                ('city', models.CharField(verbose_name='Cidade', max_length=50)),
                ('institution', models.CharField(verbose_name='Instituição', max_length=100)),
            ],
            options={
                'verbose_name': 'Enrollment',
                'verbose_name_plural': 'Enrollments',
            },
        ),
    ]
