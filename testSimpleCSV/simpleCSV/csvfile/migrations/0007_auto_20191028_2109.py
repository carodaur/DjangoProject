# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvfile', '0006_auto_20191028_2102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testclass',
            old_name='testfield1',
            new_name='employeeid',
        ),
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
