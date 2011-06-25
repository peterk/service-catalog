# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.db import models
from django.views.decorators.cache import cache_page
from katana.catalog.models import *
from django.shortcuts import render_to_response, get_object_or_404


def index(request):
    #post_list = Post.objects.all()

    #comment_list = Comment.objects.filter(is_public=True, is_removed=False).order_by('-submit_date')[:20]
    #recent_list = sorted(chain(comment_list), key=lambda item: item.submit_date)
    #recent_list.reverse()
    #recent_list = recent_list[:10]

    #recent_suggestions = Suggestion.objects.all().order_by("-id")[:10]
    #datasource_count = Dataset.objects.all().count()
    #datasource_free_count = Dataset.objects.filter(license__is_free=True).count() 
    #datasource_api_count = Dataset.objects.filter(has_api=True).count() 

    new_services = Service.objects.all().order_by("-id")[:10]
    updated_services = Service.objects.all().order_by("-id")[:10]

    page_title = u"Välkommen!"
    return render_to_response('index.html', locals())
