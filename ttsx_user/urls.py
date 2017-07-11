#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from ttsx_user import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^reg_handle/$', views.reg_handle),
    url(r'^name_verify/$', views.name_verify),
    url(r'^login/$', views.login),
    url(r'^log_handle/$', views.log_handle),
    url(r'^user_site/$', views.user_site),
    url(r'^user_info/$', views.user_info),
    url(r'^user_order/$', views.user_order),
    url(r'user_info/$', views.user_info),
    url(r'^user_islogin/$', views.user_islogin),
    url(r'^logout/$', views.logout),
]