from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import MyForm
# Create your views here.

class IndexView(View):
    def get(self,request):
        return render(request,'xuexi/register.html')
    def post(self,request):
        form = MyForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('user')
            email = form.cleaned_data.get('email')
            return HttpResponse('success')
        else:
            print(form.errors)
            return HttpResponse('fail')
