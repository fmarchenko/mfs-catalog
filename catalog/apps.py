#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Fedor Marchenko"
__email__ = "mfs90@mail.ru"
__date__ = "May 19, 2015"

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CatalogConfig(AppConfig):
    name = 'catalog'
    verbose_name = _("Catalog")