# coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class warehouse(models.Model):
	warehousename = models.CharField(u'仓库名',max_length = 20)
	warehouseinfo = models.CharField(u'仓库信息',max_length = 50)
	stock = models.CharField(u'库存',max_length = 20)
	inventory = models.CharField(u'商品种类',max_length = 20)

	def __unicode__(self):
		return self.warehousename

class goods(models.Model):
	goodsname = models.CharField(u'物品名',max_length = 20)
	goodsstock = models.CharField(u'库存',max_length = 20)
	goodsinfo = models.CharField(u'物品信息',max_length = 50)

	def __unicode__(self):
		return self.goodsname

class turnover(models.Model):
	quantity = models.CharField(u'数量',max_length = 20)
	date_time = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return self.goodsname
        
	class Meta:  #按时间下降排序
		ordering = ['-date_time']
