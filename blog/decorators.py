from django.shortcuts import render,redirect,reverse
from .models import User

#中间件到达视图之前，到了 装饰器， 这里可以直接用 中间件绑定的，request.blog_user
#所以这里不需要获取session查询数据库了，直接 判断 request里面包含blog_user 就知道登录没了
def login_requeid(func):
    def wrapper(request,*args,**kwargs):
        """
        其实这里可以直接用request.blog_user.id的，因为中间件中已经绑定过了，
        没有用就需要多一次查询了。
        # """
        # user_id = request.session.get('user_id')
        # exists = User.objects.filter(pk=user_id).exists()
        print('decorators')
        print(request.blog_user)
        if request.blog_user != None:
            return func(request,*args,**kwargs)
        else:
            return redirect(reverse('blog:login'))
    return wrapper