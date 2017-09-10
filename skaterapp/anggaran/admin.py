from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Program)
admin.site.register(Kegiatan)
admin.site.register(Paket)
admin.site.register(UsulanDanaAnggaran)