#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse

__author__ = "Fedor Marchenko"
__email__ = "mfs90@mail.ru"
__date__ = "May 19, 2015"

from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.fields import PlaceholderField
from polymorphic_tree.models import PolymorphicMPTTModel, PolymorphicTreeForeignKey
from easy_thumbnails.fields import ThumbnailerImageField


class CatalogItem(PolymorphicMPTTModel):
    name = models.CharField(_(u'название'), max_length=255)
    slug = models.SlugField(_('slug'), db_index=True)
    parent = PolymorphicTreeForeignKey(
        'self', verbose_name=_(u'родитель'), null=True, blank=True, related_name='children', db_index=True
    )

    class MPTTMeta:
        order_insertion_by = ['name']
        parent_attr = 'parent'

    class Meta:
        verbose_name = _(u'товар/услуга')
        verbose_name_plural = _(u'товары и услуги')

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('catalogitem_detail', args=[self.slug])

    @property
    def image(self):
        try:
            return self.images.all()[0].image
        except:
            return None


class CatalogContentBlock(models.Model):
    parent = models.ForeignKey(CatalogItem, related_name='contents', db_index=True)
    name = models.CharField(_(u'название'), max_length=255)
    sort_index = models.PositiveSmallIntegerField(_(u'индекс сортировки'), default=100, db_index=True)
    content = PlaceholderField('content')

    class Meta:
        ordering = ['sort_index']
        verbose_name = _('content block')
        verbose_name_plural = _('content blocks')

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.sort_index)


def get_upload_path(instance, filename):
    return '%s/%s/%s/%s' % (instance.parent.polymorphic_ctype.model, filename[:1], filename[1:3], filename)


class ItemImage(models.Model):
    parent = models.ForeignKey(CatalogItem, related_name='images', db_index=True)
    name = models.CharField(_(u'название'), max_length=255, blank=True, null=True)
    sort_index = models.PositiveSmallIntegerField(_(u'индекс сортировки'), default=100, db_index=True)
    # image = models.ImageField(_(u'изображение'), upload_to=get_upload_path)
    image = ThumbnailerImageField(_(u'изображение'), upload_to=get_upload_path)

    class Meta:
        ordering = ['sort_index']
        verbose_name = _(u'изображение')
        verbose_name_plural = _(u'изображения')

    def __unicode__(self):
        return u'%s' % self.name if self.name else self.image.name.split('/')[-1]


class Category(CatalogItem):
    class Meta:
        verbose_name = _(u'категория')
        verbose_name_plural = _(u'категории')


class Item(CatalogItem):
    unit_price = models.DecimalField(_(u'цена'), decimal_places=2, max_digits=10, default=-1)

    class Meta:
        verbose_name = _(u'товар')
        verbose_name_plural = _(u'товары')