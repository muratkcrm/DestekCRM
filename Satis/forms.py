from django import forms
from django.forms import ModelForm
from .models import SatisGorusmesi, SatisDuyurular, SatisSozlesmeler, STSsatisNotlar,STSIhaleTakip
from TalepYonetimi.models import Kurumlar, Uygulama
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class SatisGorusmesiForm(forms.ModelForm):
    class Meta:
        model = SatisGorusmesi
        SatisDosya = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        fields = ["SatisUygulama", "SatisKurum","SatisGorusulenKisi","SatisGorusulenKisiTelefon", "SatisGorusulenKisiMail","SatisKonu", "SatisAciklama", "SatisDurumu","SatisDosya"]

class SatisKurumlarForm(forms.ModelForm):
    class Meta:
        model = Kurumlar
        fields = ["KurumAdi" ,"KurumAdres","KurumIl","KurumEmail","KurumYetkili","KurumTelefon"]

class SatisUygulamaEkleForm(forms.ModelForm):
    class Meta:
        model = Uygulama
        fields = ["UygulamaAdi", "UygulamaAciklama"]

class SatisDuyuruEkleForm(forms.ModelForm):
    class Meta:
        model = SatisDuyurular
        fields = ["DuyuruBaslik", "DuyuruAciklama"]

class SatisSozlesmeEkleForm(forms.ModelForm):
    class Meta:
        model = SatisSozlesmeler
        fields = ["SozlesmeKurum","SozlesmeBaslangicTarihi","SozlesmeBitisTarihi","SozlesmeKonusu","SozlesmeDurumu"]

class SatisSozlesmeTakipForm(forms.ModelForm):
    class Meta:
        model = SatisSozlesmeler
        fields = ["SozlesmeKurum","SozlesmeBaslangicTarihi","SozlesmeBitisTarihi","SozlesmeKonusu","SozlesmeDurumu"]

class STSUserEkleForm(forms.ModelForm):
    class Meta:
        model = User
        fields =["first_name","last_name"]

class STSsatisNotlarForm(forms.ModelForm):
    class Meta:
        model = STSsatisNotlar
        satisNotDosya = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        fields = ["satisNotlarKonu","satisMetin","satisNotDosya"]

class STSIhaleTakipForm(forms.ModelForm):
    class Meta:
        model = STSIhaleTakip
        IhaleDosya = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        fields = ["IhaleYapan","IhaleYayinTarihi","IhaleAdi","IhaleAktif","IhaleDosya"]