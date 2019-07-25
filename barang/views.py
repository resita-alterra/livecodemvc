from django.shortcuts import render, redirect
from .models import Barang
from .forms import BarangForm

# Create your views here.
def home(request):
    barang = Barang.objects.all()
    return render(request,'home.html', {'barang':barang})

def lihatbarang(request, id_barang):
    tampil = Barang.objects.get(pk=id_barang)
    return render(request, 'lihatbarang.html',{'barang':tampil})

def formbarang(request):
    if request.method == 'POST':
        form = BarangForm(request.POST)
        if form.is_valid():
            post =form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = BarangForm()
    return render(request, 'inputbarang.html',{'form':form})

