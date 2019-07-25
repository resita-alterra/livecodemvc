from django import forms
from .models import Barang

class BarangForm(forms.ModelForm):
    class Meta:
        model = Barang
        fields = ('nama','harga','jenis','warna','desain','bahan','keterangan','gambar')