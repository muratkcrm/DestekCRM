from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.urls import include
from django.urls import re_path as url
from django.conf.urls.static import static

app_name = "Satis"

urlpatterns = [
    path('STSindex/', views.STSindex, name="STSindex"),
    path('Userprofil/', views.STSUserprofil, name= "STSUserprofil"),
    url(r'^UserPasswordChange/',views.STSUserPasswordChange,name = "STSUserPasswordChange"),


    path('STSgorusmeler/', views.STSgorusmeler, name="STSgorusmeler"),
    path('STSgorusmeekle/', views.STSgorusmeekle, name="STSgorusmeekle"),
    path('STSgorusmedetay/<int:id>', views.STSgorusmedetay, name="STSgorusmedetay"),

    path('STSsatisNotEkle/<int:id>', views.satisNotEkle, name="satisNotEkle"),
    path('STSsatisNotGuncelle/<int:id>', views.satisNotGuncelle, name="satisNotGuncelle"),
    path('STSsatisNotSil/<int:id>', views.satisNotSil, name="satisNotSil"),


    path('STSgorusmeguncelle/<int:id>', views.STSgorusmeguncelle, name="STSgorusmeguncelle"),
    path('STSgorusmesil/<int:id>', views.STSgorusmesil, name="STSgorusmesil"),

    path('STStekliftakip/', views.STStekliftakip, name="STStekliftakip"),
    path('STSistatistik/', views.STSistatistik, name="STSistatistik"),

    path('STSihaletakip/', views.STSihaletakip, name="STSihaletakip"),


    path('STSsozlesmetakip/', views.STSsozlesmetakip, name="STSsozlesmetakip"),
    path('STSsozlesmetakipekle/', views.STSsozlesmetakipekle, name="STSsozlesmetakipekle"),
    path('STSsozlesmetakipdetay/<int:id>', views.STSsozlesmetakipdetay, name="STSsozlesmetakipdetay"),
    path('STSsozlesmetakipguncelle/<int:id>', views.STSsozlesmetakipguncelle, name="STSsozlesmetakipguncelle"),
    path('STSsozlesmetakipsil/<int:id>', views.STSsozlesmetakipsil, name="STSsozlesmetakipsil"),

    path('STSsozlesmelerimiz/', views.STSsozlesmelerimiz, name="STSsozlesmelerimiz"),
    path('STSsozlesmeekle/', views.STSsozlesmeekle, name="STSsozlesmeekle"),
    path('STSsozlesmedetay/<int:id>', views.STSsozlesmedetay, name="STSsozlesmedetay"),
    path('STSsozlesmeguncelle/<int:id>', views.STSsozlesmeguncelle, name="STSsozlesmeguncelle"),
    path('STSsozlesmesil/<int:id>', views.STSsozlesmesil, name="STSsozlesmesil"),
    path('STSbitensozlesmeler/', views.STSbitensozlesmeler, name="STSbitensozlesmeler"),
    path('STSdevamedensozlesmeler/', views.STSdevamedensozlesmeler, name="STSdevamedensozlesmeler"),

    path('STSduyuruekle/', views.STSduyuruekle, name="STSduyuruekle"),
    path('STSduyurular/', views.STSduyurular, name="STSduyurular"),
    path('STSduyurudetay/<int:id>', views.STSduyurudetay, name="STSduyurudetay"),
    path('STSduyuruguncelle/<int:id>', views.STSduyuruguncelle, name="STSduyuruguncelle"),
    path('STSduyurusil/<int:id>', views.STSduyurusil, name="STSduyurusil"),

    path('STSkurumlar/', views.STSkurumlar, name="STSkurumlar"),
    path('STSkurumlarekle/', views.STSkurumlarekle, name="STSkurumlarekle"),
    path('STSkurumlarguncelle/<int:id>', views.STSkurumlarguncelle, name="STSkurumlarguncelle"),
    path('STSkurumlarsil/<int:id>', views.STSkurumlarsil, name="STSkurumlarsil"),
    path('STSkurumlardetay/<int:id>', views.STSkurumlardetay, name="STSkurumlardetay"),

    path('STSuygulama/', views.STSuygulama, name="STSuygulama"),
    path('STSuygulamaekle/', views.STSuygulamaekle, name="STSuygulamaekle"),
    path('STSuygulamaguncelle/<int:id>', views.STSuygulamaguncelle, name="STSuygulamaguncelle"),
    path('STSuygulamasil/<int:id>', views.STSuygulamasil, name="STSuygulamasil"),
 ]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

