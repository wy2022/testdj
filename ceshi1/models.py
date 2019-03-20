from django.db import models
from django.views import *
from django.core import validators
# Create your models here.

class user(models.Model):
    email = models.EmailField(validators=[validators.EmailValidator(message='邮箱错误',code=-1)])
    tel =models.CharField(max_length=11,validators=[validators.RegexValidator("1[345678]\d{9}",message='22请输入正确的手机号码')])
    #page 调用验证器validators 引用maxvalue和minvalue  limit_value值
    page = models.IntegerField(validators=[validators.MaxValueValidator(limit_value=10),validators.MinValueValidator(limit_value=3)])
    price = models.FloatField()


class register(models.Model):
    user =models.CharField(max_length=20)
    password =models.CharField(max_length=20)