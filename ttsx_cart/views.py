# coding=utf-8
from django.http import JsonResponse
from django.shortcuts import render

from ttsx_cart.models import CartInfo
from ttsx_user.user_decoration import islogin


@islogin
def cart(request):
    uid = request.session.get('uid')
    cart_list = CartInfo.objects.filter(user_id=uid)

    context = {'title': '购物车', 'cart_list': cart_list}
    return render(request, 'ttsx_cart/cart.html', context)


def add(request):
    try:
        # 从前端的ajax请求中获得商品id和商品数目,将其和数据库作比对.
        #
        # 如果商品不存在,则将数目和id存入数据库
        #
        # 如果商品已经存在,只需要改变商品数目,不需要再进行添加数据行
        gid = int(request.GET.get('gid'))
        count = int(request.GET.get('count', '1'))
        uid = request.session.get('uid')

        carts_list = CartInfo.objects.filter(user_id=uid, goods_id=gid)  # 查询条件要同时满足用户id和商品id
        if len(carts_list) == 1:
            cart1 = carts_list[0]
            cart1.count += count
            cart1.save()

        else:
            carts = CartInfo()
            carts.count = count
            carts.goods_id = gid
            carts.user_id = uid
            carts.save()

        return JsonResponse({'isadd': True})
    except:

        return JsonResponse({'isadd': False})


def count(request):
    uid = request.session.get('uid')
    counting = CartInfo.objects.filter(user_id=uid).count()
    return JsonResponse({'count': counting})


def editor(request):
    cid = request.GET.get('cid')
    num = request.GET.get('count')
    cart_obj = CartInfo.objects.get(pk=cid)
    cart_obj.count = num
    cart_obj.save()
    return JsonResponse({'ok': 1})


def delete(request):
    cid = request.GET.get('cid')
    cart_obj = CartInfo.objects.get(pk=cid)
    cart_obj.delete()
    return JsonResponse({'ok': 1})
