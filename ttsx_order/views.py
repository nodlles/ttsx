# coding=utf-8
from django.shortcuts import render

from ttsx_cart.models import CartInfo
from ttsx_user.models import UserInfo


def order(request):
    uid = request.session.get('uid')
    user_obj = UserInfo.objects.get(pk=uid)
    cart_obj = CartInfo.objects.filter(user_id=uid)

    context = {'title': '提交订单', 'user_info':user_obj, 'cart_info':cart_obj}
    return render(request, 'ttsx_order/place_order.html', context)
