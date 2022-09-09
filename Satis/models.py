from django.db import models
from djongo import models
from mongoengine import *
from django import forms
from django.http import HttpResponse
from ckeditor.fields import RichTextField


# Create your models here.


class SatisGorusmesi(models.Model):
    Durum_CHOICES = (('Açık', 'Açık'), ('Kapalı', 'Kapalı'), ('Geri Dönülecek', 'Geri Dönülecek'))

    id = models.AutoField(primary_key=True)
    SatisUygulama = models.ForeignKey("TalepYonetimi.Uygulama", default="1", on_delete=models.SET_NULL, null=True,verbose_name="Uygulama")
    SatisUser = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, blank=True)
    SatisKonu = models.CharField(max_length=50, verbose_name="Başlık")
    SatisGorusulenKisi = models.CharField(max_length=50,verbose_name="Yetkili Kişi")
    SatisGorusulenKisiTelefon = models.CharField(null=True, blank=True,max_length=20,verbose_name="Yetkili Telefon / Dahili")
    SatisGorusulenKisiMail = models.CharField(null=True, blank=True,max_length=50,verbose_name="Yetkili E-Posta Adresi")
    SatisKurum = models.ForeignKey("TalepYonetimi.Kurumlar", on_delete=models.SET_NULL, null=True,verbose_name="Görüşülen Kurum")
    SatisDurumu = models.CharField(default='0', choices=Durum_CHOICES, max_length=50, verbose_name="Durum")
    SatisAciklama = RichTextField(verbose_name="Açıklama")
    SatisDosya = models.FileField(blank=True, null=True, verbose_name="Çağrı Dosyası Ekle", upload_to='Dosya/')
    SatisBaslamaTarihi = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    SatisKapanmaTarihi = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    SatisAktif = models.BooleanField(default=True, verbose_name="silmek için Onayı kaldırın..!!!")

    class Meta:
        verbose_name_plural = 'Satış Görüşmeleri'
        ordering = ['-id']

    def __str__(self):
        return "%s" % (self.id)


class SatisDuyurular(models.Model):
    id = models.AutoField(primary_key=True)
    DuyuruUser = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, blank=True)
    DuyuruTarihi = models.DateTimeField(auto_now_add=True)
    DuyuruBaslik = models.CharField(max_length=250, default="", blank=True, null=True, verbose_name="Duyurunun Konusu")
    DuyuruAciklama = RichTextField(blank=True, null=True, verbose_name="Duyuru Metni")
    DuyuruAktif = models.BooleanField(default=True, verbose_name="silmek için Onayı kaldırın..!!!")


    class Meta:
        verbose_name_plural = 'Duyurular'
        ordering = ['-id']

    def __str__(self):
        return self.DuyuruBaslik


class SatisSozlesmeler(models.Model):
    Durum_CHOICES = (('Devam Eden', 'Devam Eden'), ('Süresi Biten', 'Süresi Biten'))
    id = models.AutoField(primary_key=True)

    SozlesmeUser = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, blank=True)
    SozlesmeBaslangicTarihi = models.DateField(verbose_name="Sozlesme Başlangıç Tarihi", help_text='Tarihi Girişinde örn. 22/11/2018 şeklinde / işareti koyunuz.')
    SozlesmeBitisTarihi = models.DateField(verbose_name="Sozlesme Bitiş Tarihi", help_text='Tarihi Girişinde örn. 22/11/2018 şeklinde / işareti koyunuz.')
    SozlesmeKurum = models.ForeignKey("TalepYonetimi.Kurumlar",max_length=250, on_delete=models.SET_NULL, null=True,
                                   verbose_name="Sozlesme Yapılan Kurum")
    SozlesmeKonusu = RichTextField(blank=True, null=True, verbose_name="Sozlesme Konusu")
    SozlesmeDurumu = models.CharField(default='Devam Eden', choices=Durum_CHOICES, max_length=50, verbose_name="Durum")
    SozlesmeAktif = models.BooleanField(default=True, verbose_name="silmek için Onayı kaldırın..!!!")


    class Meta:
        verbose_name_plural = 'Sözleşme Takip'
        ordering = ['-id']

    def __str__(self):
        return self.SozlesmeKurum



class STSsatisNotlar(models.Model):
    id = models.AutoField(primary_key=True)
    satisGorusmesi = models.ForeignKey(SatisGorusmesi, on_delete=models.SET_NULL, null=True, related_name="cagriNotlar")
    satisNotlarKonu = models.CharField(blank=True, null=True, max_length=50, verbose_name="Konu")
    satisMetin = RichTextField(max_length=2000, null=True, blank=False, verbose_name="İçerik",
                          help_text="Çağrı ile İlgili Tüm Notlarınızı ekleyebilirsiniz..")
    satisOlusturmaTarihi = models.DateTimeField(auto_now_add=True, null=True)
    satisNotUser = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, blank=True)
    satisNotDosya = models.FileField(blank=True, null=True, verbose_name="Çağrı Notlarına Dosya Ekle",upload_to='STSNotlar/')
    satisNotAktif = models.BooleanField(default=True, verbose_name="silmek için Onayı kaldırın..!!!")


    class Meta:
        verbose_name_plural = 'Cağrı Notları'
        ordering = ['-id']

    def __str__(self):
        return self.satisNotlarKonu

class STSIhaleTakip(models.Model):
    id = models.AutoField(primary_key=True)
    IhaleYapan = models.CharField(blank=True,null=True,max_length=550,verbose_name="İhalenin Kurumu")
    IhaleYayinTarihi = models.CharField(blank=True,null=True,max_length=550,verbose_name="İhalenin Yayın Tarihi")
    IhaleTarihi = models.CharField(blank=True,null=True,max_length=550,verbose_name="İhalenin Tarihi")
    IhaleKayitTarihi = models.DateTimeField(auto_now_add=True, null=True)
    IhaleAdi = models.CharField(blank=True,null=True,max_length=550,verbose_name="İhalenin Adı")
    IhaleAciklama = models.CharField(blank=True,null=True,max_length=550,verbose_name="İhalenin Açıklama")
    IhaleAktif = models.BooleanField(default=True, verbose_name="Biten İhale için Onayı kaldırın..!!!")
    IhaleDosya = models.FileField(blank=True, null=True, verbose_name="İhale Dosya Ekle",upload_to='IhaleTakip/')
    IhaleUser = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-IhaleTarihi']
