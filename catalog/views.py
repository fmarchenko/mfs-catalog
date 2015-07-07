#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Fedor Marchenko"
__email__ = "mfs90@mail.ru"
__date__ = "May 20, 2015"

from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView, CreateView
from django.core.urlresolvers import resolve
from django.template.context import RequestContext


class CatalogListView(ListView):
    def get_context_data(self, **kwargs):
        ctx = RequestContext(self.request, super(CatalogListView, self).get_context_data(**kwargs))
        return ctx


class CatalogDetailView(DetailView):
    def get_context_data(self, **kwargs):
        ctx = RequestContext(self.request, super(CatalogDetailView, self).get_context_data(**kwargs))
        return ctx