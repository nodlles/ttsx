from django.db import models


class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upasswd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=50, default='')
    utelephone = models.CharField(max_length=11, default='')
    uaddress = models.CharField(max_length=50, default='')
    ucode = models.CharField(max_length=6, default='')
    rname = models.CharField(max_length=20, default='')
