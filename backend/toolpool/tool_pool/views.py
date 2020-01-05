# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Listing

def index(request):
    context = {'authenticated':False}
    return render(request, 'tool_pool/page-skeleton.html', context)

def search(request):
    query = request.GET['listing-search']
    context = {'query': query}
    raw = "SELECT * FROM tool_pool_listing WHERE title LIKE '" + query + "%' ;"
    results = Listing.objects.raw(raw)
    if list(results):
        context['found'] = True
        context['result_data'] = [result.__dict__ for result in results]
    else:
        context['found'] = False
    return render(request, 'tool_pool/page-listing-search.html', context)
