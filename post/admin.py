from django.contrib import admin
from .models import Kisiler
from .models import Kitaplar
from .models import Hareketler


class KisilerAdmin(admin.ModelAdmin):
    list_display = ['adsoyad', 'sinifi', 'nosu','telefonu','email','slug']
    list_display_links = ['adsoyad', 'sinifi', 'nosu','email','telefonu']
    list_filter = ['adsoyad', 'sinifi', 'nosu','email','telefonu']
    search_fields = ['adsoyad', 'sinifi', 'nosu','email','telefonu']


class KitaplarAdmin(admin.ModelAdmin):
    list_display = ['kitapadi','yazari','yayinevi','turu','slug']
    list_display_links = ['kitapadi','yazari','yayinevi','turu']
    list_filter = ['kitapadi','yazari','yayinevi','turu']
    search_fields = ['kitapadi','yazari','yayinevi','turu']

class HareketlerAdmin(admin.ModelAdmin):
    list_display = ['adsoyad','kitapadi','alistarihi','verilistarihi','slug']
    list_display_links = ['adsoyad','kitapadi','alistarihi','verilistarihi','slug']
    list_filter = ['adsoyad','kitapadi','alistarihi','verilistarihi','slug']
    search_fields = ['adsoyad','kitapadi','alistarihi','verilistarihi','slug']

admin.site.register(Kisiler, KisilerAdmin)
admin.site.register(Kitaplar, KitaplarAdmin)
admin.site.register(Hareketler, HareketlerAdmin)