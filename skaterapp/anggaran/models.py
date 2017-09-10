from django.db import models
from django.utils import timezone

# Create your models here.
class Program(models.Model) :
    nama_program    = models.CharField(max_length=200, null = False, blank = False)

    def __str__(self):
        return self.nama_program

class Kegiatan(models.Model) :
    nama_program    = models.ForeignKey(Program)
    nama_kegiatan   = models.CharField(max_length=200, null = True, blank = True)

    def __str__ (self):
        return self.nama_kegiatan

class Paket(models.Model) :
    nama_kegiatan      = models.ForeignKey(Kegiatan)
    nama_paket         = models.CharField(max_length=300, null = True, blank = True)

    def __str__(self):
        return self.nama_paket

class UsulanDanaAnggaran(models.Model) :
    YEARS_CHOICES = (
        ('2016', '2016'),
        ('2017', '2017'),
        ('2016', '2016'),
        ('2015', '2015'),
    )

    nama_program        = models.ForeignKey(Program, null=True)
    nama_kegiatan       = models.ForeignKey(Kegiatan, null=True)
    paket               = models.ForeignKey(Paket, null=True)
    nama_usulan         = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    jumlah_anggaran     = models.DecimalField(max_digits=64, decimal_places=0, default=0)
    tahun_usulan        = models.IntegerField(choices=YEARS_CHOICES)
