#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Fedor Marchenko"
__email__ = "mfs90@mail.ru"
__date__ = "May 20, 2015"

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from . import menu


class CatalogApp(CMSApp):
    name = _('Catalog')
    urls = ['catalog.urls']
    menus = [menu.CatalogMenu]


apphook_pool.register(CatalogApp)