# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20150520_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_hot',
            field=models.BooleanField(default=False, verbose_name='\u0433\u043e\u0440\u044f\u0447\u0435\u0435 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0435'),
            preserve_default=True,
        ),
    ]
