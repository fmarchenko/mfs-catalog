#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Fedor Marchenko"
__email__ = "mfs90@mail.ru"
__date__ = "May 21, 2015"

from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu
from . import models


class CatalogMenu(CMSAttachMenu):
    name = _('catalog')

    def get_nodes(self, request):
        nodes = []
        for cat_item in models.CatalogItem.objects.all().order_by("tree_id", "lft"):
            node = NavigationNode(
                cat_item.name,
                cat_item.get_absolute_url(),
                cat_item.pk,
                cat_item.parent_id
            )
            nodes.append(node)
        return nodes


menu_pool.register_menu(CatalogMenu)