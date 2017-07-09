# coding=utf-8
from django.shortcuts import redirect


def islogin(func):
    """对于登录用户信息相关的页面，先对用户是否登录进行判断"""
    def judge(request, *args, **kwargs):
        if request.session.has_key('uid'):
            return func(request, *args, **kwargs)
        else:
            return redirect('/login/')
    return judge