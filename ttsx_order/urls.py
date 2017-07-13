#! /usr/bin/env python
# _*_ coding:utf-8 _*_

from django.conf.urls import url

from ttsx_order import views

urlpatterns = [
    url(r'^order/$', views.order),

]