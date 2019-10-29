# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvfile', '0010_auto_20191028_2135'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Testclass',
        ),
    ]
