from django.urls import path
from . import views
app_name ='blog'
urlpatterns = [
    path('', views.index,name='index'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('music/',views.music,name='music'),
    path('video/',views.VideoView.as_view(),name='video'),
    path('loginout/',views.loginOut,name='loginout'),
    path('test/',views.test)
]
