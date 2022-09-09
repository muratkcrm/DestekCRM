from django import forms
from django.forms import ModelForm
from .models import DestekTalebiKayit,DestekTalebiTuru,Uygulama,Kurumlar,KurumBirimi,Kategori,Kisi, Duyurular, DestekTalebiNotlar
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey


class DestekTalebiForm(forms.ModelForm):
    class Meta:
        model = DestekTalebiKayit
        list_display =  ["DestekTalebiUygulama", "DestekTalebiKonu","DestekTalebiTuruAdi","DestekTalebiKategori", "DestekTalebiKurum", "DestekTalebiBirim", "DestekTalebiKisi","DestekTalebiDurumu","DestekTalebiAciklama","DestekTalebiDosya"]
        search_fields = ['DestekTalebiKonu','DestekTalebiAciklama']
        #error_css_class = 'error'
        DestekTalebiDosya = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        fields = ["DestekTalebiUygulama", "DestekTalebiKonu","DestekTalebiTuruAdi","DestekTalebiKategori", "DestekTalebiKurum", "DestekTalebiBirim", "DestekTalebiKisi","DestekTalebiKisiTelefon","DestekTalebiTfsId","DestekTalebiDurumu","DestekTalebiAciklama","DestekTalebiDosya"]

        #fields = '__all__'           ---- kullanılabilen alanların hepsini al
        #exclude = ['DestekTalebiUygulama']  ----  haric tümünü al

class DestekTalebiNotlarForm(forms.ModelForm):
    class Meta:
        model = DestekTalebiNotlar
        DestekTalebiNotDosya = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        fields = ["DestekTalebiNotlarKonu","Metin","DestekTalebiNotDosya"]

class KisiEkleForm(forms.ModelForm):
    class Meta:
        model = Kisi
        file = forms.FileField()
        list_display =["KisiAdiSoyadi","KurumAdi","KisiBirimAdi","KisiTelefon","KisiEmail"]
        fields= ["KisiAdiSoyadi","KurumAdi","KisiBirimAdi","KisiBirimAdi","KisiTelefon","KisiEmail",]

class KurumlarEkleForm(forms.ModelForm):
    class Meta:
        model = Kurumlar
        fields = ["id","KurumAdi" ,"KurumAdres","KurumIl","KurumEmail","KurumYetkili","KurumTelefon"]


class KurumBirimiEkleForm(forms.ModelForm):
    class Meta:
        model = KurumBirimi
        fields = ('id','KurumAdi', 'BirimAdi', 'BirimAdresi', 'BirimEmail', 'BirimYetkili', 'BirimTelefon')


class UygulamaEkleForm(forms.ModelForm):
    class Meta:
        model = Uygulama
        fields = ["UygulamaAdi", "UygulamaAciklama"]

class DestekTalebiTuruEkleForm(forms.ModelForm):
    class Meta:
        model = DestekTalebiTuru
        fields = ["DestekTalebiAdi", "DestekTalebiAciklama"]

class KategoriEkleForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ["KategoriAdi", "KategoriAciklama"]

class DuyuruEkleForm(forms.ModelForm):
    class Meta:
        model = Duyurular
        fields = ["DuyuruBaslik", "DuyuruAciklama"]

class DuyuruEklefullForm(forms.ModelForm):
    class Meta:
        model = Duyurular
        fields = ["DuyuruBaslik", "DuyuruAciklama","DuyuruUygulama"]

class DuyuruGuncelleForm(forms.ModelForm):
    class Meta:
        model = Duyurular
        fields = ["DuyuruBaslik", "DuyuruAciklama","DuyuruUygulama","DuyuruAktif"]

class UserEkleForm(forms.ModelForm):
    class Meta:
        model = User
        fields =["first_name","last_name","email"]


