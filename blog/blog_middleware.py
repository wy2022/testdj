from .models import  User
from django.shortcuts import redirect,reverse

#到达视图之前，把需要的参数放在request里面
def blog_middle(get_response):
    print('初始化')
##初始化代码
    def middleware(request):
        user_id = request.session.get('user_id')
        userModel = User.objects.filter(pk=user_id).first()
        print(userModel)
        if userModel:
            print('userModel true')
            setattr(request,'blog_user',userModel)
        else:
            print('userModel None')
            setattr(request,'blog_user',None)

        #request  到达 view之前的代码

        print('到view之前')
        response = get_response(request)
        print('到浏览器之前')
#到达浏览器前执行的代码from .models import  User
        return response
    return middleware