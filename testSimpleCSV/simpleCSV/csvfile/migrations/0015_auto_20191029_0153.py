# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvfile', '0014_auto_20191028_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportIDChecklist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reportid', models.IntegerField()),
            ],
            options={
                'db_table': 'reportidchecklist',
            },
        ),
        migrations.DeleteModel(
            name='Testclass',
        ),
    ]
