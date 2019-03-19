from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=200,verbose_name='姓名')
    wangming = models.CharField(max_length=200,verbose_name='网名')
    zhiye = models.CharField(max_length=200,verbose_name='职业')
    address = models.CharField(max_length=500,verbose_name='地址')
    email = models.EmailField(max_length=200,verbose_name='邮箱')
    qq = models.IntegerField(default=1,verbose_name='QQ')
    weixin = models.CharField(max_length=200,verbose_name='微信')
    class Meta:
        verbose_name_plural='用户'
    def __str__(self):
        return self.wangming
class fenlei(models.Model):
    name =models.CharField(max_length=200,verbose_name='名称')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='分类'

class biaoqian(models.Model):
    name = models.CharField(max_length=200,verbose_name='名称')
    class Meta:
        verbose_name_plural='标签'
    def __str__(self):
        return self.name
class wenzhang(models.Model):
    title = models.CharField(max_length=500,verbose_name='标题')
    neirong = HTMLField(verbose_name='内容1')
    img =models.ImageField(upload_to='img/%Y%m%d',verbose_name='图片路径')
    dianji = models.IntegerField(default=1,verbose_name='点击量')
    zhiding = models.BooleanField(default=False,verbose_name='推荐')
    insert_time = models.DateTimeField(auto_now_add=True,verbose_name='时间')
    uesr = models.ForeignKey(user,related_name='user',on_delete=models.CASCADE,verbose_name='作者')
    fenlei = models.ForeignKey(fenlei,related_name='fenlei',on_delete=models.CASCADE,verbose_name='分类')
    biaoqian = models.ForeignKey(biaoqian,related_name='biaoqian',on_delete=models.CASCADE,verbose_name='标签')
    class Meta:
        verbose_name_plural='文章'


    def __str__(self):
        return self.title

