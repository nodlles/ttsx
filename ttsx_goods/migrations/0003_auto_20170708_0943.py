# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttsx_goods', '0002_auto_20170707_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gclick',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpice',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gstock',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gsubtitle',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gtitle',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gunit',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='typeinfo',
            name='ttitle',
            field=models.CharField(max_length=10),
        ),
    ]
