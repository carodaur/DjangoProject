# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20191025_0355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='thumb',
        ),
    ]
