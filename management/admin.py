from django.contrib import admin
from .models import warehouse, goods, turnover

# Register your models here.
admin.site.register(warehouse)
admin.site.register(goods)
admin.site.register(turnover)