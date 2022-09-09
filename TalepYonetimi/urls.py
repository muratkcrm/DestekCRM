from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.urls import re_path as url
from django.conf.urls.static import static

app_name = "TalepYonetimi"

urlpatterns = [
    path('TLPindex/', views.TLPindex, name="TLPindex"),
    path('Userprofil/', views.TLPUserprofil, name="Userprofil"),
    url(r'^UserPasswordChange/', views.TLPUserPasswordChange, name="UserPasswordChange"),

    path('TLPkayitacik/', views.kayitacik, name="kayitacik"),
    path('TLPkayitkapali/', views.kayitkapali, name="kayitkapali"),
    path('TLPkayitEkle/', views.kayitEkle, name="kayitEkle"),
    path('TLPkayitGuncelle/<int:id>', views.kayitGuncelle, name="kayitGuncelle"),
    path('TLPkayitSil/<int:id>', views.kayitSil, name="kayitSil"),
    path('TLPkayitDetay/<int:id>', views.kayitDetay, name="kayitDetay"),

    path('TLPDestekTalebiNotEkle/<int:id>', views.DestekTalebiNotEkle, name="DestekTalebiNotEkle"),
    path('TLPDestekTalebiNotGuncelle/<int:id>', views.DestekTalebiNotGuncelle, name="DestekTalebiNotGuncelle"),
    path('TLPDestekTalebiNotSil/<int:id>', views.DestekTalebiNotSil, name="DestekTalebiNotSil"),

    path('TLPDestekTalebiIstatistik/', views.DestekTalebiIstatistik, name="DestekTalebiIstatistik"),

    path('TLPkurumlar/', views.kurumlar, name="kurumlar"),
    path('TLPkurumlarEkle/', views.kurumlarEkle, name="kurumlarEkle"),
    path('TLPkurumlarGuncelle/<int:id>', views.kurumlarGuncelle, name="kurumlarGuncelle"),
    path('TLPkurumlarSil/<int:id>', views.kurumlarSil, name="kurumlarSil"),
    path('TLPkurumlarDetay/<int:id>', views.KurumlarDetay, name="kurumlarDetay"),

    path('TLPkurumBirimi/', views.kurumBirimi, name="kurumBirimi"),
    path('TLPkurumBirimiEkle/', views.kurumBirimiEkle, name="kurumBirimiEkle"),
    path('TLPkurumBirimiGuncelle/<int:id>', views.kurumBirimiGuncelle, name="kurumBirimiGuncelle"),
    path('TLPkurumBirimiSil/<int:id>', views.kurumBirimiSil, name="kurumBirimiSil"),
    path('TLPkurumBirimiDetay/<int:id>', views.KurumBirimiDetay, name="KurumBirimiDetay"),

    path('TLPuygulama/', views.uygulama, name="uygulama"),
    path('TLPuygulamaEkle/', views.uygulamaEkle, name="uygulamaEkle"),
    path('TLPuygulamaGuncelle/<int:id>', views.uygulamaGuncelle, name="uygulamaGuncelle"),
    path('TLPuygulamaSil/<int:id>', views.uygulamaSil, name="uygulamaSil"),

    path('TLPDestekTalebiTuru/', views.destekTalebiTuru, name="DestekTalebiTuru"),
    path('TLPDestekTalebiTuruEkle/', views.DestekTalebiTuruEkle, name="DestekTalebiTuruEkle"),
    path('TLPDestekTalebiTuruGuncelle/<int:id>', views.DestekTalebiTuruGuncelle, name="DestekTalebiTuruGuncelle"),
    path('TLPDestekTalebiTuruSil/<int:id>', views.DestekTalebiTuruSil, name="DestekTalebiTuruSil"),

    path('TLPkategori/', views.kategori, name="kategori"),
    path('TLPkategoriEkle/', views.kategoriEkle, name="kategoriEkle"),
    path('TLPkategoriGuncelle/<int:id>', views.kategoriGuncelle, name="kategoriGuncelle"),
    path('TLPkategoriSil/<int:id>', views.kategoriSil, name="kategoriSil"),

    path('TLPkisi/', views.kisi, name="kisi"),
    path('TLPkisiEkle/', views.kisiEkle, name="kisiEkle"),
    path('TLPkisiGuncelle/<int:id>', views.kisiGuncelle, name="kisiGuncelle"),
    path('TLPkisiSil/<int:id>', views.kisiSil, name="kisiSil"),
    path('TLPkisiDetay/<int:id>', views.kisiDetay, name="kisiDetay"),


    path('TLPDuyuruEkle/', views.duyuruEkle, name="duyuruEkle"),
    path('TLPDuyurular/', views.duyurular, name="duyurular"),
    path('TLPDuyuruDetay/<int:id>', views.DuyuruDetay, name="DuyuruDetay"),
    path('TLPDuyuruGuncelle/<int:id>', views.duyuruGuncelle, name="DuyuruGuncelleme"),

    url(r'^csv/$', views.export_csv, name='export_csv'),
    url(r'^xls/$', views.export_xls, name='export_xls'),
 ]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

