# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import csv
from .models import User, Rating, Listing

def index(request):
    context = {'authenticated':False}
    return render(request, 'tool_pool/page-skeleton.html', context)

def search(request):
    query = request.GET['listing-search']
    context = {'query': query}
    raw =  "SELECT * FROM tool_pool_listing WHERE title LIKE '%" + query + "%' ;"
    results = Listing.objects.raw(raw)
    if list(results):
        users = {x.pk:x for x in User.objects.all()}
        context['found'] = True
        context['result_data'] = [result.__dict__ for result in results]
        for result in context['result_data']:
            result['poster'] = users[result['poster_id']]
    else:
        context['found'] = False
    return render(request, 'tool_pool/page-listing-search.html', context)

def test(request):
    with open('../../sample_data.csv') as f:
        reader = csv.reader(f)
        next(reader, None)
        next(reader, None)
        for row in reader:
                if all('' in s for s in row[1:]):
                    break
                _, created = User.objects.get_or_create(
                    username=row[0],
                    display_name=row[1],
                    location=row[2],
                    contactinfo=row[3]
                    )
                _.listing_set.create(
                    title=row[11],
                    type=row[12],
                    deposit=row[13],
                    upfrontcost=row[14],
                    ratecost=row[15],
                    rateinterval=row[16],
                    currentavailable=row[17],
                    maxavailable=row[18],
                    pluscode=row[19],
                    contactinfo=row[20],
                    details=row[21],
                    imagecount=row[22],
                    visible=row[23].capitalize()
                    )
    return HttpResponse("Complete")
