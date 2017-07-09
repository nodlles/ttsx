# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gtitle', models.CharField(max_length=30)),
                ('gpic', models.ImageField(upload_to=b'goods/')),
                ('gpice', models.DecimalField(max_digits=5, decimal_places=3)),
                ('gclick', models.IntegerField()),
                ('gunit', models.BooleanField(max_length=30)),
                ('isDelete', models.BooleanField(default=False)),
                ('gsubtitle', models.CharField(max_length=300)),
                ('gstock', models.IntegerField(default=300)),
                ('gcontent', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ttitle', models.CharField(max_length=30)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(to='ttsx_goods.TypeInfo'),
        ),
    ]
