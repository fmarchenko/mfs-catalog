#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Fedor Marchenko"
__email__ = "mfs90@mail.ru"
__date__ = "May 19, 2015"
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from polymorphic_tree.admin import PolymorphicMPTTParentModelAdmin, PolymorphicMPTTChildModelAdmin
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.widgets import ImageClearableFileInput
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from cms.admin.placeholderadmin import FrontendEditableAdminMixin
from . import models


class ItemImageAdminInline(admin.TabularInline):
    model = models.ItemImage
    formfield_overrides = {
        ThumbnailerImageField: {'widget': ImageClearableFileInput},
    }


class CatalogContentBlockAdminInline(PlaceholderAdminMixin, FrontendEditableAdminMixin, admin.TabularInline):
    model = models.CatalogContentBlock


class CatalogChildAdmin(PolymorphicMPTTChildModelAdmin):
    GENERAL_FIELDSET = (None, {
        'fields': ('name', 'slug', 'parent'),
    })

    base_model = models.CatalogItem
    base_fieldsets = (
        GENERAL_FIELDSET,
    )

    prepopulated_fields = {'slug': ('name',)}
    inlines = [CatalogContentBlockAdminInline, ItemImageAdminInline]


class CatalogParentAdmin(PolymorphicMPTTParentModelAdmin):
    base_model = models.CatalogItem
    child_models = (
        (models.Category, CatalogChildAdmin),
        (models.Item, CatalogChildAdmin),
    )

    list_display = ('name', 'actions_column',)

    class Media:
        css = {
            'all': ('catalog/admin/css/admin.css',)
        }


admin.site.register(models.CatalogItem, CatalogParentAdmin)