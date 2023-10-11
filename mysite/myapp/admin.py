from django.contrib import admin
from .models import Product

# Register your models here.
#здесь регистрация собственных слассов моделей базы данных, что бы они видны были ы админ панели
admin.site.register(Product)


