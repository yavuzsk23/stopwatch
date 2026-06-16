from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# Basit bir fonksiyon yazdik
def ana_sayfa(request):
    return HttpResponse("<h1>Selam kanka! Bu benim ilk Django sitem. RTX 5060 ile ucuyoruz!</h1>")

urlpatterns = [
    path('admin/', admin.py),
    path('', ana_sayfa), # Ana sayfa bos oldugunda fonksiyonu calistir
]
