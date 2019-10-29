# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvfile', '0012_delete_payrolllist'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayrollList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employeeid', models.IntegerField()),
                ('payperiod', models.CharField(max_length=24)),
                ('amountpaid', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'payrolllist',
            },
        ),
        migrations.CreateModel(
            name='Testclass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employeeid', models.IntegerField()),
            ],
            options={
                'db_table': 'testclass',
            },
        ),
    ]
