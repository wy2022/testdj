from django.urls import path,include

from . import views
urlpatterns = [
    path('',views.indexView.as_view()),
    path('register/',views.registerView.as_view()),
    path('upload/',views.UploadView.as_view()),
    path('img/',views.imgView.as_view()),
]
