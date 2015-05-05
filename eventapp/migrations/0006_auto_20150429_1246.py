# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0005_auto_20150429_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobil',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
