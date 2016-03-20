from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class warehouse(models.Model):
	warehousename = models.CharField(max_length = 20)
	warehouseinfo = models.CharField(max_length = 50)
	stock = models.CharField(max_length = 20)
	inventory = models.CharField(max_length = 20)

	def __unicode__(self):
        return self.warehousename

class goods(models.Model):
	goodsname = models.CharField(max_length = 20)
	goodsstock = models.CharField(max_length = 20)
	goodsinfo = models.CharField(max_length = 50)

	def __unicode__(self):
        return self.goodsname

class turnover(models.Model):
	quantity = models.CharField(max_length = 20)
	date_time = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
        return self.goodsname
        
    class Meta:  #按时间下降排序
        ordering = ['-date_time']
