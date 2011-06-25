# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

catalogindex = url(
    regex  = '^$',
    view   = 'katana.catalog.views.index',
    name   = 'vwcatalogindex'
)

urlpatterns = patterns('', catalogindex)

