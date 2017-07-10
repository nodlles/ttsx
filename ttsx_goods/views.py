#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.paginator import Paginator
from django.shortcuts import render
from ttsx_goods.models import TypeInfo, GoodsInfo


def index(request):
    """商品首页"""
    type_list = TypeInfo.objects.all()  # 查询出所有类别
    context_list = []
    for kind in type_list:  # 查询出每个列别对应的所有商品，按id和点击量降序排列
        new_list = kind.goodsinfo_set.order_by('-id')[0:4]  # 取出前四个
        click_list = kind.goodsinfo_set.order_by('-gclick')[0:4]  # 取出前四个
        context_list.append({'new_list':new_list, 'click_list': click_list, 'kind':kind})  # 将两种排序组合为字典
    context = {'title': '首页', 'context_list': context_list}
    return render(request, 'ttsx_goods/index.html', context)


def lists(request, kid, pindex, orderby):
    """商品列表页"""
    order_str = '-id'
    if orderby == '2':
        order_str = 'gpic'
    elif orderby == '3':
        order_str = 'gclick'
    kind = TypeInfo.objects.get(pk=int(kid))
    new_list = kind.goodsinfo_set.order_by('-id')[0:2]
    all_list = kind.goodsinfo_set.order_by(order_str)
    paginator = Paginator(all_list, 4)  # 返回分页对象，all_list为列表数据，16是每页数据的条数
    page = paginator.page(int(pindex))  # 方法page(m)：返回Page对象，表示第m页的数据，下标以1开始
    context = {'title': '天天生鲜-商品列表', 'kind': kind, 'new_list': new_list, 'all_list': all_list,
               'page': page, 'orderby': orderby}
    return render(request, 'ttsx_goods/list.html', context)


def detail(request, gid):
    """商品详情页"""
    try:
        goods = GoodsInfo.objects.get(pk=int(gid))
        new_goods = goods.gtype.goodsinfo_set.order_by('-id')[0:2]

        context = {'title': '商品详情页', 'new_goods': new_goods, 'goods': goods}
        return render(request, 'ttsx_goods/detail.html', context)
    except :
        return render(request, '404.html')