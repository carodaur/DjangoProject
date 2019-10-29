# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvfile', '0013_payrolllist_testclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='testclass',
            name='amountpaid',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AddField(
            model_name='testclass',
            name='payperiod',
            field=models.CharField(default=b'', max_length=24),
        ),
    ]
