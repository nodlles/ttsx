# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttsx_user', '0001_initial'),
        ('ttsx_goods', '0005_auto_20170708_1602'),
        ('ttsx_cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(to='ttsx_goods.GoodsInfo')),
                ('user', models.ForeignKey(to='ttsx_user.UserInfo')),
            ],
        ),
        migrations.RemoveField(
            model_name='carsinfo',
            name='goods',
        ),
        migrations.RemoveField(
            model_name='carsinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='CarsInfo',
        ),
    ]
