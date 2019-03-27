from .models import User
#定义上下文处理器 比如用户登录后，各个页面都需要用户信息
def blog_user(request):
    user_id = request.session.get('user_id')
    context = {}
    if user_id:
        try:
            user_info = User.objects.get(pk=user_id)
            context['user_info'] = user_info
        except:
            pass
    #上下文处理器必须要返回一个字典 这样views 就
    return context
