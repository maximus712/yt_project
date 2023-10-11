from django.urls import path
from .views import index, indexItem

app_name = 'myapp'
#базовый начальный шаблон http://127.0.0.1:8000/myapp/ от него строим оствльные
#динамический путь строиться через heelo/<int:somevalue(id,it,hgg and some)>/
urlpatterns = [
    path('',index),
    path('<int:id>/',indexItem,name='detail'),
   
]