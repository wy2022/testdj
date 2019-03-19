from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import *
from django.db.models import F,Q
from django.views.generic import ListView,DetailView
# Create your views here.


def index(request):
    user_mx = user.objects.get(pk=1)
    wz_count= wenzhang.objects.count()
    request.session['wz_count']=wz_count
    request.session['author']=user_mx.wangming
    wzlist =wenzhang.objects.all().order_by('-insert_time')[:4]
    fenlei_all =fenlei.objects.all()
    wzph = wenzhang.objects.all().order_by('-dianji')[:5]
    zhiding =wenzhang.objects.filter(zhiding=1).order_by('-insert_time')[:2]
    context = {
        'user': user_mx,
        'wenzhang': wzlist,
        'fenlei_all': fenlei_all,
        'paihang':wzph,
        'zhiding':zhiding
    }

    return render(request,'boke/index.html',context)


def article(request,id):
    wenzhang.objects.filter(id=id).update(dianji=F('dianji')+1)
    wz_mx = wenzhang.objects.get(id=id)
    wzph = wenzhang.objects.filter(fenlei_id=wz_mx.fenlei_id).order_by('-dianji')
    next_wz = wenzhang.objects.filter(id=id+1)
    up_wz = wenzhang.objects.filter(id=id-1)
    xiangguan_wz = wenzhang.objects.filter(fenlei=wz_mx.fenlei)
    context = {
        'wenzhang':wz_mx,
        'paihang':wzph,
        'next':next_wz,
        'up':up_wz,
        'xiangguan_wz':xiangguan_wz,
    }
    return render(request,'boke/info.html',context)


class wzlistView(ListView):
    # model = fenlei
    template_name = 'boke/list.html'
    context_object_name = 'wenzhang'
    paginate_by = 4
    # ordering = '-insert_time' #不知道为什么 负不管用
    def get_queryset(self):
        self.fenlei_id = self.kwargs['fenlei_id']
        return wenzhang.objects.filter(fenlei__exact=self.fenlei_id).order_by('-insert_time')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['biaoqian'] = biaoqian.objects.all()
        context['fenleiid']=self.fenlei_id
        return context



class biaoqianView(ListView):
    template_name = 'boke/list.html'
    context_object_name = 'wenzhang'
    paginate_by = 4
    def get_queryset(self):
        self.biaoqian = self.kwargs['biaoqian_id']
        return wenzhang.objects.filter(biaoqian__exact=self.biaoqian).order_by('-insert_time')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['biaoqian'] = biaoqian.objects.all()
        context['biaoqianid']=self.biaoqian
        return context

class searchView(ListView):
    template_name = 'boke/list.html'
    context_object_name = 'wenzhang'
    paginate_by = 4
    def get_queryset(self):
        # print(self.kwargs['text'])
        # self.text = self.kwargs['text']
        self.text = self.request.GET['text']

        return wenzhang.objects.filter(Q(neirong__icontains=self.text)|Q(title__icontains=self.text))
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['biaoqian'] = biaoqian.objects.all()
        context['sousuo']=self.text
        return context

