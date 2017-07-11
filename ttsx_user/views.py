# coding=utf-8
import hashlib
import datetime
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from ttsx_goods.models import GoodsInfo
from ttsx_user.models import UserInfo
# from django.contrib.auth import login, authenticate
from user_decoration import islogin


def register(request):
    return render(request, 'ttsx_user/register.html')


def reg_handle(request):
    uname = request.POST.get('user_name')
    passwd = request.POST.get('user_pwd')
    email = request.POST.get('user_email')
    sha1 = hashlib.sha1()
    sha1.update(passwd)
    upasswd = sha1.hexdigest()
    user = UserInfo()
    user.uname = uname
    user.upasswd = upasswd
    user.uemail = email
    user.save()
    return redirect('/login/')


def name_verify(request):
    uname = request.GET.get('uname')
    res = UserInfo.objects.filter(uname=uname).count()
    context = {'res': res}
    return JsonResponse(context)


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'uname': uname}
    return render(request, 'ttsx_user/login.html', context)


def log_handle(request):
    uname = request.POST.get('username')
    passwd = request.POST.get('pwd')
    hold = request.POST.get('hold', 0)  # 默认值为
    user = UserInfo.objects.filter(uname=uname)
    sha1 = hashlib.sha1()
    sha1.update(passwd)
    upasswd = sha1.hexdigest()
    context = {'uname': uname}  # 传入前段数据
    if len(user) == 0:
        context['user_error'] = '此用户还未注册'
        return render(request, 'ttsx_user/login.html', context)
    else:
        if user[0].upasswd == upasswd:  # 密码验证成功之后
            response = redirect(request.session.get('url_path', '/index/'))
            # response = redirect('/user_info/')
            request.session['uid'] = user[0].id  # 记录用户登录状态 讲用户id写入session
            request.session['uname'] = user[0].uname  #
            if hold == '1':
                response.set_cookie('uname', uname,
                                    expires=datetime.datetime.now()+datetime.timedelta(days=14))  # 设置过期时间
            else:
                response.set_cookie('uname', '', max_age=-1)
            return response
        else:
            context['pwd_error'] = '密码错误'
            return render(request, 'ttsx_user/login.html', context)


def logout(request):
    request.session.flush()
    return redirect('/index/')


@islogin
def user_site(request):
    user = UserInfo.objects.get(pk=request.session['uid'])
    if request.method == 'POST':  # post请求，修改当前用户对象的收货信息
        post=request.POST
        rname=post.get('rname')
        uaddress=post.get('uaddress')
        ucode=post.get('ucode')
        utelephone=post.get('uphone')

        user.uaddress = uaddress
        user.ucode = ucode
        user.utelephone = utelephone
        user.rname = rname
        user.save()

    context={'user': user, 'title': '收货地址'}
    return render(request, 'ttsx_user/user_center_site.html', context)


@islogin
def user_info(request):
    user = UserInfo.objects.get(pk=request.session['uid'])

    goods = request.COOKIES.get('good_ids', '')
    id_list = goods.split('_')[:-1]
    glist = []
    for id in id_list:
        glist.append(GoodsInfo.objects.get(id=id))
    context = {'user': user, 'title': '个人信息', 'glist': glist}
    return render(request, 'ttsx_user/user_center_info.html', context)


@islogin
def user_order(request):
    context = {'title': '全部订单'}
    return render(request, 'ttsx_user/user_center_order.html', context)

# def center(request):
#     user=UserInfo.objects.get(pk=request.session['uid'])
#     context={'user':user}
#     return render(request,'ttsx_user/center.html',context)
# def order(request):
#     context={}
#     return render(request,'ttsx_user/order.html',context)
# def site(request):
#     user = UserInfo.objects.get(pk=request.session['uid'])
#     if request.method=='POST':#post请求，修改当前用户对象的收货信息
#         post=request.POST
#         ushou=post.get('ushou')
#         uaddress=post.get('uaddress')
#         ucode=post.get('ucode')
#         uphone=post.get('uphone')

    #     user.ushou=ushou
    #     user.uaddress=uaddress
    #     user.ucode=ucode
    #     user.uphone=uphone
    #     user.save()
    # context={'user':user}
    # return render(request,'ttsx_user/site.html',context)
