# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvfile', '0003_payroll'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testclass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('testfield1', models.IntegerField()),
            ],
            options={
                'db_table': 'testclass',
            },
        ),
    ]
