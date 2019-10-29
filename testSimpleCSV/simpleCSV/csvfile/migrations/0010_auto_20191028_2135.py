# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvfile', '0009_auto_20191028_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testclass',
            name='amountpaid',
        ),
        migrations.RemoveField(
            model_name='testclass',
            name='payperiod',
        ),
    ]
