from django.db import models

# Create your models here.
class Barang(models.Model):
    nama = models.CharField(max_length=255)
    harga = models.IntegerField()
    jenis = models.CharField(max_length=255)
    warna = models.CharField(max_length=255)
    desain = models.CharField(max_length=255)
    bahan = models.CharField(max_length=255)
    keterangan = models.TextField()
    gambar = models.URLField()