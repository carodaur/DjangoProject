# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workschedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('hoursworked', models.DecimalField(max_digits=5, decimal_places=2)),
                ('employeeid', models.IntegerField()),
                ('jobgroup', models.CharField(max_length=1)),
            ],
        ),
    ]
