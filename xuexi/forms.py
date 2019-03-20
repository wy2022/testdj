from django import forms
#
class MyForm(forms.Form):
    user = forms.CharField(max_length=10,min_length=3,error_messages={"max_lenth":"uesr length 》3 了"})
    email = forms.EmailField(label="邮箱")
