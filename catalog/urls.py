#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Fedor Marchenko"
__email__ = "mfs90@mail.ru"
__date__ = "May 20, 2015"

from django.conf.urls import *
from . import views
from . import models

urlpatterns = patterns('',
    url(r'^hot/$', views.ListView.as_view(queryset=models.Item.objects.filter(is_hot=True)), name='hotitem_list'),
    url(r'^(?P<slug>.*)/$', views.DetailView.as_view(model=models.CatalogItem), name='catalogitem_detail'),
    url(r'^$', views.ListView.as_view(queryset=models.CatalogItem.objects.filter(parent__isnull=True)), name='catalogitem_list'),
)