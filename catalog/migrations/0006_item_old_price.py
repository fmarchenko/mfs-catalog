# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_item_is_hot'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='old_price',
            field=models.DecimalField(default=-1, verbose_name='\u0441\u0442\u0430\u0440\u0430\u044f \u0446\u0435\u043d\u0430', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
    ]
