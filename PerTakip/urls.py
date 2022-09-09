from . import views
from django.conf import settings
from django.urls import path, include
from django.urls import re_path as url
from django.conf.urls.static import static

app_name = "PerTakip"

urlpatterns = [
    path('PTKindex/', views.PTKindex, name="PTKindex"),
    path('Userprofil/', views.PTKUserprofil, name="PTKUserprofil"),
    path('UserPasswordChange/', views.PTKUserPasswordChange, name="PTKPasswordChange"),

    path('PTKkayitacik/', views.PTKkayitacik, name="PTKkayitacik"),
    path('PTKkayitacikizindurum/', views.PTKkayitacikizindurum, name="PTKkayitacikizindurum"),
    path('PTKkayitkapaliizindurum/', views.PTKkayitkapaliizindurum, name="PTKkayitkapaliizindurum"),
    path('PTKkayitizinDetay/<int:id>', views.PTKkayitizinDetay, name="PTKkayitizinDetay"),
    
    path('PTKkayitkapali/', views.PTKkayitkapali, name="PTKkayitkapali"),
    path('PTKkayitEkle/', views.PTKkayitEkle, name="PTKkayitEkle"),
    path('PTKkayitGuncelle/<int:id>', views.PTKkayitGuncelle, name="PTKkayitGuncelle"),
    path('PTKkayitSil/<int:id>', views.PTKkayitSil, name="PTKkayitSil"),
    path('PTKkayitDetay/<int:id>', views.PTKkayitDetay, name="PTKkayitDetay"),

    path('PTKkayitHesaplama/<int:id>', views.PTKkayitHesaplama, name="PTKkayitHesaplama"),

    path('PTKDuyuruEkle/', views.PTKduyuruEkle, name="PTKduyuruEkle"),
    path('PTKDuyurular/', views.PTKduyurular, name="PTKduyurular"),
    path('PTKDuyuruDetay/<int:id>', views.PTKDuyuruDetay, name="PTKDuyuruDetay"),
    path('PTKDuyuruGuncelle/<int:id>', views.PTKduyuruGuncelle, name="PTKDuyuruGuncelleme"),

    path('PTKkayitNotEkle/<int:id>', views.PTKkayitNotEkle, name="PTKkayitNotEkle"),
    path('PTKkayitNotGuncelle/<int:id>', views.PTKkayitNotGuncelle, name="PTKkayitNotGuncelle"),
    path('PTKkayitNotSil/<int:id>', views.PTKkayitNotSil, name="PTKkayitNotSil"),

    #url(r'^csv/$', views.export_csv, name='export_csv'),
    url(r'^xls/$', views.export_xls, name='export_xls'),
    url(r'^ayrilanxls/$', views.export_ayrilanxls, name='export_ayrilanxls'),

    path('PTKIzinKayit/', views.PTKIzinKayit, name="PTKIzinKayit"),
    path('PTKIzinEkle/', views.PTKIzinEkle, name="PTKIzinEkle"),
    path('PTKIzinGuncelle/<int:id>', views.PTKIzinGuncelle, name="PTKIzinGuncelle"),
    path('PTKIzinSil/<int:id>', views.PTKIzinSil, name="PTKIzinSil"),
    path('PTKIzinDetay/<int:id>', views.PTKIzinDetay, name="PTKIzinDetay"),
    

    #url(r'^izinxls/$', views.export_ayrilanxls, name='export_ayrilanxls')


]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
