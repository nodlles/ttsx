# coding=utf-8
from django.http import JsonResponse
from django.shortcuts import render

from ttsx_cart.models import CartInfo


def cart(request):

    context = {'title': '购物车'}
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
    cart = CartInfo.objects.get(id=uid)
    count = cart.count
    return JsonResponse({'count': count})
