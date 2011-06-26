# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

catalogindex = url(
    regex  = '^$',
    view   = 'katana.catalog.views.index',
    name   = 'vwcatalogindex'
)

catalogservice = url(
    regex  = '^(?P<service_id>\d+)/$',
    view   = 'katana.catalog.views.service',
    name   = 'vwcatalogservice'
)

urlpatterns = patterns('', catalogindex, catalogservice)

