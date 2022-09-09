from django.urls import path, include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "Yonetim"

urlpatterns = [
    path('YONindex/', views.YONindex, name="YONindex"),
    path('YONkurumlar/', views.YONkurumlar, name="YONkurumlar"),
    path('YONkurumlarGuncelle/<int:id>', views.YONkurumlarGuncelle, name="YONkurumlarGuncelle"),

    path('YONkurumBirimi/', views.YONkurumBirimi, name="YONkurumBirimi"),
    path('YONkurumBirimiGuncelle/<int:id>', views.YONkurumBirimiGuncelle, name="YONkurumBirimiGuncelle"),

    path('YONuygulama/', views.YONuygulama, name="YONuygulama"),
    path('YONuygulamaGuncelle/<int:id>', views.YONuygulamaGuncelle, name="YONuygulamaGuncelle"),

    path('YONdestekTalebiTuru/', views.YONdestekTalebiTuru, name="YONdestekTalebiTuru"),
    path('YONdestekTalebiTuruGuncelle/<int:id>', views.YONdestekTalebiTuruGuncelle, name="YONdestekTalebiTuruGuncelle"),

    path('YONkategori/', views.YONkategori, name="YONkategori"),
    path('YONkategoriGuncelle/<int:id>', views.YONkategoriGuncelle, name="YONkategoriGuncelle"),

    path('YONkisi/', views.YONkisi, name="YONkisi"),
    path('YONkisiGuncelle/<int:id>', views.YONkisiGuncelle, name="YONkisiGuncelle"),

    path('YONstskurumlar/', views.YONstskurumlar, name="YONstskurumlar"),
    path('YONstskurumlarGuncelle/<int:id>', views.YONstskurumlarGuncelle, name="YONstskurumlarGuncelle"),

    path('YONstsuygulama/', views.YONstsuygulama, name="YONstsuygulama"),
    path('YONstsuygulamaGuncelle/<int:id>', views.YONstsuygulamaGuncelle, name="YONstsuygulamaGuncelle"),

    path('YONonmcarihesap/', views.YONonmcarihesap, name="YONonmcarihesap"),
    path('YONonmcarihesapGuncelle/<int:id>', views.YONonmcarihesapGuncelle, name="YONonmcarihesapGuncelle"),

    path('YONonmhesapplani/', views.YONonmhesapplani, name="YONonmhesapplani"),
    path('YONonmhesapplaniGuncelle/<int:id>', views.YONonmhesapplaniGuncelle, name="YONonmhesapplaniGuncelle"),

    path('YONonmstokkart/', views.YONonmstokkart, name="YONonmstokkart"),
    path('YONonmstokkartGuncelle/<int:id>', views.YONonmstokkartGuncelle, name="YONonmstokkartGuncelle"),

    path('YONPertakip/', views.YONPertakip, name="YONPertakip"),
    path('YONPertakipGuncelle/<int:id>', views.YONPertakipGuncelle, name="YONPertakipGuncelle"),

    path('YONUserPasswordChange/', views.YONUserPasswordChange, name="YONUserPasswordChange"),

    path('YONregister/', views.YONregister, name="YONregister"),
    path('UserparolarReset/<int:id>', views.YONKullaniciSifre, name="YONKullaniciSifre"),
    path('YONregisterEkle/', views.YONregisterEkle, name="YONregisterEkle"),
    path('YONregisterGuncelle/<int:id>', views.YONregisterGuncelle, name="YONregisterGuncelle"),

    path('YONUserPasswordChange/', views.YONUserPasswordChange, name="YONUserPasswordChange"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)