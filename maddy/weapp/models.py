
from django.db import models
from django.contrib import admin
class Order(models.Model):
    order_no=models.IntegerField(primary_key=True)
    category=models.CharField()
    product_name=models.CharField(max_length=15)
    quantity=models.IntegerField()
    price=models.FloatField()
    address=models.TextField()
    phone_no=models.IntegerField()
class OrderAdmin(admin.ModelAdmin):
    list_display=["order_no","category","product_name","quantity","price","address","phone_no"]

