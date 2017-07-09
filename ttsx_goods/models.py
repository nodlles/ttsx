#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from tinymce.models import HTMLField


class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=10)
    isDelete = models.BooleanField(default=False)


class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=50)
    gpic = models.ImageField(upload_to='goods/')
    gpice = models.DecimalField(max_digits=5, decimal_places=2)
    gclick = models.IntegerField(default=0)
    gunit = models.CharField(max_length=10)
    isDelete = models.BooleanField(default=False)
    gsubtitle = models.CharField(max_length=200)
    gstock = models.IntegerField(default=100)
    gcontent = HTMLField()
    gtype = models.ForeignKey('TypeInfo')