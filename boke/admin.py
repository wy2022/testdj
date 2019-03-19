from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(user)
class userInfo(admin.ModelAdmin):
    list_display = ['id','name','wangming','zhiye','address','email','qq','weixin']
    list_display_links =  ['id','name','wangming','zhiye','address','email','qq','weixin']
@admin.register(wenzhang)
class wenzhangInfo(admin.ModelAdmin):
    list_display = ['id','title','dianji','zhiding','insert_time','fenlei','biaoqian']
    list_display_links = ['title','dianji']
    search_fields = ['title','neirong']
    # list_editable = ['dianji','zhiding','fenlei','biaoqian']
    list_editable = ['zhiding','fenlei','biaoqian']
    list_filter = ['uesr']
    readonly_fields = ['dianji']

@admin.register(fenlei)
class fenleiInfo(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(biaoqian)
class biaoqianInfo(admin.ModelAdmin):
    list_display = ['id','name']
# admin.site.register(user)
# admin.site.register(fenlei)
# admin.site.register(wenzhang)
# admin.site.register(biaoqian)
