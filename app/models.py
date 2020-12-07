from django.db import models

# Create your models here.

from django.db.models import ForeignKey, CharField
from datetime import datetime 

from datetime import datetime,date,time
import time

class Uyeler(models.Model):
    nick_name = models.CharField(max_length=50,verbose_name="Nick Name")
    e_mail= models.EmailField(max_length=100,verbose_name="Üye E-mail")
    password = models.CharField(max_length=50,verbose_name="Üye Giriş Parolası")
    bugday=models.IntegerField(verbose_name="Bugday Adet",default=0)
    cozulen_soru=models.IntegerField(verbose_name="Çözülen Soru",default=0)
    uyelik_tarihi=models.DateTimeField(auto_now_add=True,verbose_name="Üye Olma Tarihi")
    forget=models.CharField(max_length=20,verbose_name="Forget Link",blank=True)
    gsm=models.CharField(max_length=50,verbose_name="Gsm",blank=True)

    def __str__(self):
        return self.nick_name

class Kategori(models.Model):
    isim= models.CharField(max_length=50,verbose_name="Kategori ismi")
    aciklama= models.CharField(max_length=300,verbose_name="Kategori Açıklama",blank=True,default="aaa")
    resim=models.FileField(upload_to='kategori_resim/',blank=True,verbose_name="Kategori Resim")
    resim_alt= models.CharField(max_length=100,verbose_name="Resim Alt Açıklama",default="Buğday Bağışla")


    def __str__(self):
        return self.isim

class Grup(models.Model):
    isim= models.CharField(max_length=50,verbose_name="Grup İsim")
    resim=models.FileField(upload_to='grup_resim/',blank=True,verbose_name="Grup Resim")
    grup_bugday=models.IntegerField(verbose_name="Grup Toplam Buğday",default=0)

    def __str__(self):
        return self.isim

class Soru(models.Model):
    kategori=models.ForeignKey("Kategori",on_delete=models.CASCADE)
    soru=CharField(max_length=500,verbose_name="Soru")
    sik_1=CharField(max_length=500,verbose_name="Şık 1 (Doğru Cevap)")
    sik_2=CharField(max_length=500,verbose_name="Şık 2")
    sik_3=CharField(max_length=500,verbose_name="Şık 3")
    sik_4=CharField(max_length=500,verbose_name="Şık 4")

    def __str__(self):
        return str(self.kategori)

class Ayarlar(models.Model):

    gunluk=models.IntegerField(verbose_name="Günlük Toplam",default=0)
    aylik=models.IntegerField(verbose_name="Aylık Toplam",default=0)
    toplam=models.IntegerField(verbose_name="Ömürlük Toplam Buğday",default=0)
    gunluk_toplam=models.IntegerField(verbose_name="Günlük Toplam Buğday",default=0)
    gunluk_ziyaretci=models.IntegerField(verbose_name="Günlük Ziyaretçi",default=0)
    gunluk_cozulen_soru=models.IntegerField(verbose_name="Günlük Çözülen Soru",default=0)
    toplam_ziyaretci=models.IntegerField(verbose_name="Toplam Ziyaretçi",default=0)
    cozulen_soru=models.IntegerField(verbose_name="Toplam Çözülen Soru",default=0)
    toplam_soru_sayisi=models.IntegerField(verbose_name="Toplam Soru Sayisi",default=0)


    def __str__(self):
        return "Ayarlar"

class Iletisim(models.Model):
    kadi= models.CharField(max_length=500,verbose_name="Kullanıcı Adı")
    kbasi=models.CharField(max_length=500,verbose_name="Konu Başlığı")
    kicerik=models.CharField(max_length=5000,verbose_name="Konu İçeriği")

    def __str__(self):
        return self.kbasi

