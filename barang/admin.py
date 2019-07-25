from django.contrib import admin
from .models import Barang

# Register your models here.
class BarangAdmin(admin.ModelAdmin):
    list_display = ['id','nama','harga','jenis','gambar']

admin.site.register(Barang,BarangAdmin)