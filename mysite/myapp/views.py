from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product #подключили модели из приложения 

# Create your views here.
#Здесь создаем функции предатсавления наших страниц, после их определения переходим в myapp/urls 
#и прописываем путь и указываем отсюда функцию которую хотим отобразить на странице

def index(request):
    #получили в items все названия обьектов моделей созданных 
    items = Product.objects.all() 
   
    context = {
        'items':items
        
    } 
    return render(request,'myapp/index.html',context=context)

#context - это способ передать обьект в выбрвнный шаблон
def indexItem(request,id):
    item = Product.objects.get(id=id)
    
    context = {
        'item':item
    } 
    return render(request,'myapp/detail.html',context=context)


