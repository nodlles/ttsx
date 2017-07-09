#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from ttsx_goods.models import TypeInfo, GoodsInfo


class TypeInfoAdmin(admin.ModelAdmin):
    def __str__(self):
        return self.ttitle
    list_display = ['id', 'ttitle', 'isDelete']


class GoodsInfoAdmin(admin.ModelAdmin):
    def __str__(self):
        return self.gtitle
    list_display = ['id', 'gtitle', 'gpice', 'gstock']


admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)
