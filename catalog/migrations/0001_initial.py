# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields
import polymorphic_tree.models
import catalog.models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20150419_1006'),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
            ],
            options={
                'ordering': ('tree_id', 'lft'),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('catalogitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='catalog.CatalogItem')),
            ],
            options={
                'verbose_name': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
            bases=('catalog.catalogitem',),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('catalogitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='catalog.CatalogItem')),
                ('unit_price', models.DecimalField(verbose_name='\u0446\u0435\u043d\u0430', max_digits=10, decimal_places=2)),
            ],
            options={
                'verbose_name': '\u0442\u043e\u0432\u0430\u0440',
                'verbose_name_plural': '\u0442\u043e\u0432\u0430\u0440\u044b',
            },
            bases=('catalog.catalogitem',),
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', blank=True)),
                ('sort_index', models.PositiveSmallIntegerField(default=100, verbose_name='\u0438\u043d\u0434\u0435\u043a\u0441 \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438', db_index=True)),
                ('image', models.ImageField(upload_to=catalog.models.get_upload_path, verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('parent', models.ForeignKey(related_name='images', to='catalog.CatalogItem')),
            ],
            options={
                'ordering': ['sort_index'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='catalogitem',
            name='content',
            field=cms.models.fields.PlaceholderField(slotname=b'service_content', editable=False, to='cms.Placeholder', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='catalogitem',
            name='parent',
            field=polymorphic_tree.models.PolymorphicTreeForeignKey(related_name='children', blank=True, to='catalog.CatalogItem', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='catalogitem',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_catalog.catalogitem_set+', editable=False, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
    ]
