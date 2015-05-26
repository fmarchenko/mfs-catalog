# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import catalog.models
import polymorphic_tree.models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalogitem',
            options={'verbose_name': '\u0442\u043e\u0432\u0430\u0440/\u0443\u0441\u043b\u0443\u0433\u0430', 'verbose_name_plural': '\u0442\u043e\u0432\u0430\u0440\u044b \u0438 \u0443\u0441\u043b\u0443\u0433\u0438'},
        ),
        migrations.AlterModelOptions(
            name='itemimage',
            options={'ordering': ['sort_index'], 'verbose_name': '\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', 'verbose_name_plural': '\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f'},
        ),
        migrations.AlterField(
            model_name='catalogitem',
            name='parent',
            field=polymorphic_tree.models.PolymorphicTreeForeignKey(related_name='children', verbose_name='\u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044c', blank=True, to='catalog.CatalogItem', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='unit_price',
            field=models.DecimalField(default=-1, verbose_name='\u0446\u0435\u043d\u0430', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='itemimage',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=catalog.models.get_upload_path, verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435'),
            preserve_default=True,
        ),
    ]
