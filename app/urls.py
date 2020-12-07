from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static
import string

#path('register/<int:ref>', views.register, name='default'),

urlpatterns = [
path('', views.index, name='index'),
path('kontrol', views.kontrol, name='kontrol'),
path('giris', views.giris, name='giris'),
path('giris-form', views.giris_form, name='giris form'),
path('cikis', views.cikis, name='cikis'),
path('uye-ol', views.uye_ol, name='uye ol'),
path('uye-ol-form', views.uye_ol_form, name='uye ol form'),
path('hakkimizda', views.hakkimizda, name='hakkimizda'),
path('hakkimizda/<str:sayfa>', views.hakkimizda_sayfa, name='hakkimizda sayfa'),
path('kategoriler', views.kategoriler, name='kategoriler'),
path('kategoriler/<int:idd>', views.kategoriler_id, name='kategoriler Alt index'),
path('kategoriler/<str:kisim>/<int:idd>', views.kategoriler_id_isim, name='kategoriler Alt index isimli'),
path('lider-tablosu', views.lider_tablosu, name='lider tablosu'),
path('iletisim', views.iletisim, name='iletisim'),
path('iletisim-form', views.iletisim_form, name='iletisim form'),
path('gizlilik-sozlesmesi', views.gizlilik, name='gizlilik sözleşmesi'),
path('uyelik-sozlesmesi', views.uyelik, name='üyelik sözleşmesi'),
path('soru-cevap/<int:soru>', views.soru_cevap, name='Soru Cevap'),
path('soru-cevap/<str:kategori>/<str:metin>/<int:soru>', views.soru_cevap_metin, name='Soru Cevap'),
path('random-soru', views.random_soru, name='Random Soru'),
path('sitemap.xml', views.sitemap, name='Sitemap'),
path('sitemap_<int:sira>.xml', views.sitemap_sira, name='Sitemap Sira'),
path('robot.txt', views.robot_txt, name='Robot'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)