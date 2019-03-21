from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import *
import json
# Create your views here.

class indexView(View):
    def get(self,request):
        return  render(request,'ceshi1/index.html')
        # return HttpResponse('get')
    def post(self,request):
        form =MyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
        else:
            print(form.get_errors())
            # print(form.errors)
            # print(form.errors.get_json_data())
            return HttpResponse('fail')

class registerView(View):
    def get(self,request):
        return HttpResponse('get ok')

    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            #commit 意思得到save 数据库这个对象，不直接更新数据库
            user = form.save(commit=False)
            user.password = form.cleaned_data.get('pwd1')
            user.save()
            return HttpResponse('ok')
        else:
            print(form.errors.get_json_data())
            #给字典转换成json
            s =form.errors.get_json_data()
            print(json.dumps(s))
            return HttpResponse('fail')

class UploadView(View):
    def get(self,request):
        return render(request,'ceshi1/upload.html')
    def post(self,request):
        form = uploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('ok')
        else:
            print(form.errors.get_json_data)
            return HttpResponse('fail')

class imgView(View):
    def get(self,request):
        return render(request,'ceshi1/img.html')
    def post(self,request):
        form = imgForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
        else:
            print(form.errors.get_json_data)
            return HttpResponse('fail')
