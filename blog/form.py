from django import forms
from .models import User
from django.db.models import Q

class RegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=11,min_length=6)
    password1 = forms.CharField(max_length=11,min_length=6)
    #重写clean方法，获取密码对比下
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password1 = cleaned_data.get('password1')
        tel = cleaned_data.get('tel')
        username =cleaned_data.get('username')
        user_list = User.objects.filter(Q(username__exact=username) | Q(tel__exact=tel)).first()
        # print(user_list)
        if user_list != None:
            raise forms.ValidationError(message='用户名或者手机号重复')
        if len(str(tel)) != 11:
            raise forms.ValidationError(message='手机号错误')
        if password != password1:
            raise forms.ValidationError(message='密码不一致')
        return cleaned_data
    class Meta:
        model = User
        fields = '__all__'
