from django.contrib import admin
from .models import *

# Register your models here.

class UyelerAdmin(admin.ModelAdmin):
    search_fields =["nick_name","e_mail"]
    list_display =["nick_name","e_mail","bugday","gsm"]

    class Meta:
        model = Uyeler

class KategoriAdmin(admin.ModelAdmin):
    list_display =["isim"]

    class Meta:
        model = Kategori

class GrupAdmin(admin.ModelAdmin):

    list_display =["isim"]

    class Meta:
        model = Grup

class SoruAdmin(admin.ModelAdmin):
    search_fields =["soru","kategori__isim","sik_1","sik_2","sik_3","sik_4"]
    list_display =["soru","kategori","sik_1","sik_2","sik_3","sik_4"]

    class Meta:
        model = Soru

class IletisimAdmin(admin.ModelAdmin):

    list_display =["kadi","kbasi","kicerik"]

    class Meta:
        model = Iletisim



admin.site.register(Uyeler, UyelerAdmin)
#admin.site.register(Kategori, KategoriAdmin)
#admin.site.register(Grup, GrupAdmin)
admin.site.register(Soru, SoruAdmin)
admin.site.register(Iletisim, IletisimAdmin)
admin.site.register(Ayarlar)
