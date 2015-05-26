# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20150520_1547'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalogcontentblock',
            options={'ordering': ['sort_index'], 'verbose_name': 'content block', 'verbose_name_plural': 'content blocks'},
        ),
        migrations.AddField(
            model_name='catalogitem',
            name='slug',
            field=models.SlugField(default='24', verbose_name='slug'),
            preserve_default=False,
        ),
    ]
