# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20150419_1006'),
        ('catalog', '0002_auto_20150520_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogContentBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('sort_index', models.PositiveSmallIntegerField(default=100, verbose_name='\u0438\u043d\u0434\u0435\u043a\u0441 \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438', db_index=True)),
                ('content', cms.models.fields.PlaceholderField(slotname=b'content', editable=False, to='cms.Placeholder', null=True)),
                ('parent', models.ForeignKey(related_name='contents', to='catalog.CatalogItem')),
            ],
            options={
                'ordering': ['sort_index'],
                'verbose_name': 'content',
                'verbose_name_plural': 'contents',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='catalogitem',
            name='content',
        ),
    ]
