from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('barang/<int:id_barang>', views.lihatbarang,name='lihat'),
    path('form/', views.formbarang, name='form'),
]