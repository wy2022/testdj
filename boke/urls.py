from django.urls import path
from . import views
from testdj import settings
from django.conf.urls.static import static
app_name='boke'
urlpatterns = [
    path('', views.index,name='index'),
    path('article/<int:id>', views.article,name='article'),
    path('list/<fenlei_id>/',views.wzlistView.as_view(), name='list'),
    path('biaoqian/<biaoqian_id>/',views.biaoqianView.as_view(),name='biaoqian'),
    path('search/<str:text>/',views.searchView.as_view(),name='search'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
