# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvfile', '0004_testclass'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Payroll',
            new_name='PayrollList',
        ),
    ]
