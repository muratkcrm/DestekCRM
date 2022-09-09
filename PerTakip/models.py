from sqlite3 import Date
from django.db import models
from djongo import models
from mongoengine import *
connect('PerTakip')
from django import forms
from django.http import HttpResponse
from ckeditor.fields import RichTextField
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField




class PerTakipKayit(models.Model):
    Durum_CHOICES = (('Çalışıyor', 'Çalışıyor'), ('Ayrıldı', 'Ayrıldı'))

    id = models.AutoField(primary_key=True)
    PTKTckimlik = models.CharField(null=False, blank=True,max_length=250, verbose_name="Tc Kimlik No")
    PTKAdiSoyadi = models.CharField(blank=True, null=False, max_length=250, verbose_name="Personel Adı-Soyadı")
    PTKFirmaAdi = models.ForeignKey("PTKFirma", default=1, on_delete=models.SET_NULL, null=True, verbose_name="Hangi Firmada")
    PTKIseGiristarihi = models.DateField(blank=True, verbose_name="İşe Giriş Tarihi :")
    PTKIseCikistarihi = models.DateField(blank=True, null=True, verbose_name="İşe Çıkış Tarihi :")
    PTKAdres = models.CharField(blank=True, null=True, max_length=250, verbose_name="Adres")
    PTKIl = models.CharField(blank=True, null=True, max_length=50, verbose_name= "İl")
    PTKIlce = models.CharField(blank=True, null=True, max_length=50, verbose_name="İlçe")
    PTKEmail = models.EmailField(blank=True, null=True, verbose_name="Email" )
    PTKTelefon = models.CharField(blank=True, null=True, max_length=50, verbose_name="Telefon")
    PTKGorevi = models.CharField(blank=True, null=True, max_length=50, verbose_name="Personel Görevi")
    PTKAciklama = models.CharField(blank=True, null=True, max_length=2000, verbose_name="Açıklama")
    PTKHakedilenIzinYil = models.IntegerField (default=0,null=True, blank=True, verbose_name="Hakedilen İzin Yıl")
    PTKHakedilenIzinGun = models.IntegerField (default=0,null=True, blank=True, verbose_name="Hakedilen İzin Süresi Gün")
    PTKIzinSuresiGun = models.IntegerField (default=0,null=True, blank=True, verbose_name="Kullanılan İzin Süresi Gün")
    PTKkalanizin = models.IntegerField (default=0,null=True, blank=True, verbose_name="Kullanılan İzin Süresi Gün")
    PTKIzinSuresiSaat = models.FloatField (default=0,null=True, blank=True, verbose_name="Kullanılan İzin Süresi Saat")
    PTKDosya = models.FileField(blank=True, null=True, verbose_name="Not ile ilgili dosya ekle", upload_to='Dosya/Not/')
    PTKAktif = models.BooleanField(default=True, verbose_name="silmek için Onayı kaldırın..!!!")
    PTKDurumu = models.CharField(default='Çalışıyor', choices=Durum_CHOICES, max_length=50, verbose_name="Çalışıyor Mu ?")
    PTKOluşturmatarihi = models.DateTimeField(auto_now_add=True, null=True)
    PTKModifiyeTarihi = models.DateTimeField(editable=False, null=True, blank=True)
    PTKKayitUser = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, blank=True,verbose_name="Talebi Açan Kullanıcı")

    class Meta:
        
        verbose_name_plural = 'Personel kayıt girişi'
        ordering = ['id']

    def __str__(self):
        return self.PTKAdiSoyadi


class PerIzinDurum(models.Model):
    id = models.AutoField(primary_key=True)
    PerTakipKayit = models.ForeignKey(PerTakipKayit, on_delete=models.SET_NULL, null=True)
    PerAdiSoyadi = models.CharField(blank=True, null=True, max_length=250, verbose_name="Personel Adı-Soyadı")
    PerIzinDonemi = models.CharField(default= "2022", blank=True, null=True, max_length=10 ,verbose_name="Personel Kullanılan İzin Dönemi :")
    PerIzinBaslatarihi = models.DateField(blank=True, verbose_name="Personel İzin Başlangıç Tarihi :")
    PerIzinBitistarihi = models.DateField(blank=True, null=True, verbose_name="Personel İzin Bitiş Tarihi :")
    PerIzinKonu = models.CharField(max_length=50, verbose_name="İzin Nedeni")
    PerIzinSuresiGun = models.IntegerField (default=0,null=True, blank=True, verbose_name="İzin Süresi Gün")
    PerIzinSuresiSaat = models.IntegerField (default=0,null=True, blank=True, verbose_name="İzin Süresi Saat")
    PerIzinOnayVeren = models.CharField(default="Oktay Bey",max_length=50, verbose_name="İzin Onaylayan")
    PerIzinOluşturmatarihi = models.DateTimeField(auto_now_add=True, null=True)
    PerIzinModifiyeTarihi = models.DateTimeField(editable=False, null=True, blank=True)
    #PerIzinMetin = RichTextField(max_length=2000, null=False, blank=False, verbose_name="İçerik",help_text="izin ilgili notları ekleyebilirsiniz..")
    PerIzinUser = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, blank=True)
    PerIzinDosya = models.FileField(blank=True, null=True, verbose_name="İzin Formu Dosya ya Ekle", upload_to='Izinler/')
    PerIzinAktif = models.BooleanField(default=True, verbose_name="silmek için Onayı kaldırın..!!!")

    
    class Meta:
        verbose_name_plural = 'Personel izin girişi'
        ordering = ['-id']
        

class PerIzinHakedis(models.Model):
    id = models.AutoField(primary_key=True)
    PerTakipKayit = models.ForeignKey(PerTakipKayit, on_delete=models.SET_NULL, null=True)
    PerIzinHakedisDonemi = models.CharField(default= "2022", blank=True, null=True, max_length=10 ,verbose_name="Personel İzin Hakediş Dönemi :")
    PerIzinHakedistarihi = models.DateField(blank=True, null=True, verbose_name="Personel İzin Hakediş Tarihi :")
    PerIzinHakedilenSure = models.FloatField (null=True, blank=True)
    PerIzinHakedisOluşturmatarihi = models.DateTimeField(auto_now_add=True, null=True)
    PerIzinHakedisModifiyeTarihi = models.DateTimeField(editable=False, null=True, blank=True)
    PerIzinHakedisUser = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, blank=True)
    PerIzinHakedisAktif = models.BooleanField(default=True, verbose_name="silmek için Onayı kaldırın..!!!")

    class Meta:
        verbose_name_plural = 'Personel Hakedilen İzin'
        ordering = ['-id']



class PTKDuyurular(models.Model):
    id = models.AutoField(primary_key=True)
    PTKDuyuruUser = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, blank=True)
    PTKDuyuruTarihi = models.DateTimeField(auto_now_add=True)
    PTKDuyuruBaslik = models.CharField(max_length=250, default="", verbose_name="Duyurunun Konusu")
    PTKDuyuruAciklama = RichTextField(blank=True, null=True, verbose_name="Duyuru Metni")
    PTKDuyuruAktif = models.BooleanField(default=True, verbose_name="silmek için Onayı kaldırın..!!!")

    class Meta:
        verbose_name_plural = 'PTKDuyurular'
        ordering = ['-id']

    def __str__(self):
        return self.PTKDuyuruBaslik


class PerTakipNotlar(models.Model):
    id = models.AutoField(primary_key=True)
    PerTakipKayit = models.ForeignKey(PerTakipKayit, on_delete=models.SET_NULL, null=True, related_name="DestekTalebiNotlar")
    PerTakipNotlarKonu = models.CharField( max_length=50, verbose_name="Konu")
    PerTakipMetin = RichTextField(max_length=2000, null=True, blank=False, verbose_name="İçerik",
                          help_text="Çağrı ile İlgili Tüm Notlarınızı ekleyebilirsiniz..")
    PerTakipOlusturmaTarihi = models.DateTimeField(auto_now_add=True, null=True)
    PerTakipNotUser = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, blank=True)
    PerTakipNotDosya = models.FileField(blank=True, null=True, verbose_name="Çağrı Notlarına Dosya Ekle",upload_to='Notlar/')
    PerTakipNotAktif = models.BooleanField(default=True, verbose_name="silmek için Onayı kaldırın..!!!")

    class Meta:
        verbose_name_plural = 'Personel Notları'
        ordering = ['-id']

    def __str__(self):
        return self.PerTakipNotlarKonu

class PTKFirma(models.Model):
    id = models.AutoField(primary_key=True)
    PTKFirmaUser = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, blank=True)
    PTKFirmaTarihi = models.DateTimeField(auto_now_add=True)
    PTKFirmaAdi = models.CharField(max_length=250, default="", verbose_name="Firma Adını giriniz")
    PTKFirmaAciklama = RichTextField(blank=True, null=True, verbose_name="Firma Bilgisi")
    PTKFirmaAktif = models.BooleanField(default=True, verbose_name="silmek için Onayı kaldırın..!!!")

    def __str__(self):
        return self.PTKFirmaAdi


