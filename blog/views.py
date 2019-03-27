from django.shortcuts import render,HttpResponse,redirect,reverse
from django.core.cache import cache
from django.views import View
from .form import RegisterForm
from .models import User
from django.contrib import messages #引入消息，返回前端错误信息
from .decorators import login_requeid
from django.utils.decorators import method_decorator
# Create your views here.
@login_requeid
def index(request):

    return render(request,'blog/index.html')


class LoginView(View):
    def get(self,request):
        return render(request,'blog/login.html')
    def post(self,request):
        useranme = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username__exact=useranme, password__exact=password).first()
        if user:
            request.session['user_id'] =user.id
            #设置session 关闭浏览器后过期
            request.session.set_expiry(0)

            return redirect(reverse('blog:index'))
        else:
            print('帐号密码错误')
            messages.info(request,'帐号密码错误')
            #如果登录失败 重定向到登录
            return redirect(reverse('blog:login'))

def loginOut(request):
    del request.session['user_id']
    return redirect(reverse('blog:login'))
class RegisterView(View):
    def get(self,request):
        return render(request,'blog/register.html')
    def post(self,request):
        #用验证器验证下 输入的信息
        Form = RegisterForm(request.POST)
        if Form.is_valid():
            Form.save()
            return render(request, 'blog/login.html')
        else:
            err = Form.errors.get_json_data()
            print(err)
            return HttpResponse('注册失败')

@login_requeid
def music(request):

    return render(request,'blog/music.html')


# @login_requeid
# def video(request):
#     return render(request,'blog/video.html')
@method_decorator(login_requeid,name='dispatch')
#dispathc 类视图中所有方法都用这个，name='get' name='post' 也可以 直接在 方法中写装饰器
class VideoView(View):
    def get(self,request):

        return render(request, 'blog/video.html')
    # @method_decorator(login_requeid)  类上面写也行，如果想指定某一个 方法用装饰器可以这样写
    def post(self,request):
        return render(request, 'blog/video.html')
def test(request):
    from django.http import HttpResponseNotFound
    from django.http import HttpResponse
    # return HttpResponseNotFound('weizhaodao')
    return HttpResponse('ssssd',status=202)