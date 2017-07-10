#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from ttsx_goods import views

urlpatterns =[
    url(r'^index/$', views.index),
    url(r'^lists(\d+)_(\d+)_(\d+)/$', views.lists),
    url(r'^detail(\d+)/$',views.detail),
]