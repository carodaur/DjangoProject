# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvfile', '0008_auto_20191028_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payrolllist',
            name='amountpaid',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='payrolllist',
            name='payperiod',
            field=models.CharField(max_length=24),
        ),
    ]
