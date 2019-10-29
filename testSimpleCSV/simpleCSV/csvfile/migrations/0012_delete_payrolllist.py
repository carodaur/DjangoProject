# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvfile', '0011_delete_testclass'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PayrollList',
        ),
    ]
