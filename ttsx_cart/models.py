from django.db import models

from ttsx_goods.models import GoodsInfo
from ttsx_user.models import UserInfo


class CartInfo(models.Model):
    user = models.ForeignKey(UserInfo)
    goods = models.ForeignKey(GoodsInfo)
    count = models.IntegerField()