# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    display_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    contactinfo = models.TextField()

class Rating(models.Model):
    to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    _from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    value = models.IntegerField()

class Listing(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    brb = [('BUY','Buy'),
          ('REN', 'Rent'),
          ('BOR', 'Borrow')]
    type = models.CharField(max_length=3, choices=brb)
    deposit = models.IntegerField()
    upfrontcost = models.IntegerField()
    ratecost = models.IntegerField()
    rateinterval = models.CharField(max_length=40)
    currentavailable = models.IntegerField()
    maxavailable = models.IntegerField()
    pluscode = models.CharField(max_length=10)
    contactinfo = models.TextField()
    details = models.TextField()
    imagecount = models.IntegerField()
    visible = models.BooleanField()
