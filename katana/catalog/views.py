# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.db import models
from django.views.decorators.cache import cache_page
from katana.catalog.models import *
from django.shortcuts import render_to_response, get_object_or_404


def index(request):
    new_services = Service.objects.all().order_by("-id")[:10]
    updated_services = Service.objects.all().order_by("-id")[:10]

    page_title = u"Välkommen till tjänstekatalogen!"
    return render_to_response('index.html', locals())


def service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    page_title = service.name + " av " + service.contact_person.organization.name
    return render_to_response('service.html', locals())
