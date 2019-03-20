from django import forms
from .models import *


# class Myform(forms.Form):
#     # account = forms.CharFiled(max_length=10,min_length=3,error_message={"max_length":"cuwou"})

class MyForm(forms.ModelForm):
    #这里可以直接修改models的 page 然后判断，抛出异常
    def clean_page(self):
        page = self.cleaned_data.get('page')
        if page >5:
            raise forms.ValidationError('页面不能大于5')
        return page

    class Meta:
        model = user
        fields = '__all__'
        #不适用默认提示，
        error_messages ={
           'tel':{
               'required':'电话必须填写',
               'max_value':'最大11个'
            },
            'email':{
                'invalid':'无效',
                'required':'必须写'
            }
        }
    #写个函数，把错误信息放到字典字典，方便前端用
    def get_errors(self):
        errors = self.errors.get_json_data()
        new_errors = {}
        for key,message_dicts in errors.items():
            messages=[]
            for message_dict in message_dicts:
                message = message_dict['message']
                messages.append(message)
            new_errors[key] = messages
        return new_errors

#注册时输入两次密码判断是否一致
class RegisterForm(forms.ModelForm):
    pwd1 = forms.CharField(max_length=20,min_length=5)
    pwd2 = forms.CharField(max_length=20,min_length=5)
    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError(message='两次密码不一致!!',code=-1)
        return cleaned_data
    class Meta:
        model = register
        exclude =['password']

