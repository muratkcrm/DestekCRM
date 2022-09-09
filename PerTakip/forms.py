from bootstrap3_datetime.widgets import DateTimePicker
from bootstrap_datepicker.widgets import DatePicker
import django_filters
from django import forms
from django.forms import DateInput, ModelForm
from matplotlib import widgets
from .models import PerIzinHakedis, PerTakipKayit, PTKDuyurular, PerTakipNotlar, PerIzinDurum
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'
    
class DatePickerInput(forms.DateInput):
    input_type = 'date'

class TimePickerInput(forms.TimeInput):
    input_type = 'time'

class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime'

class PerTakipKayitEklemeForm(forms.ModelForm):
    class Meta:
        model = PerTakipKayit
        PTKTckimlik = forms.IntegerField(max_value=99999999999)
        #PTKIseGiristarihi = forms.DateField(widget=DatePickerInput)
        #PTKIseCikistarihi = forms.DateTimeField(widget=DateTimePickerInput)
        PTKEmail = forms.EmailField()
        PTKDosya = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        fields = ["PTKTckimlik","PTKAdiSoyadi","PTKFirmaAdi","PTKIseGiristarihi","PTKIseCikistarihi","PTKAdres","PTKIlce", "PTKIl","PTKEmail","PTKTelefon","PTKAciklama","PTKDurumu"]
        widgets = {
            'PTKIseGiristarihi' : forms.DateInput(
                format=('%d-%m-%Y'),
                attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
            'PTKIseCikistarihi' : forms.DateInput(
                format=('%d-%m-%Y'),
                attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
        }

class PerTakipKayitForm(forms.ModelForm):
    class Meta:
        model = PerTakipKayit
        PTKTckimlik = forms.IntegerField(max_value=99999999999)
        PTKIseGiristarihi = forms.DateField(widget=DatePickerInput)
        PTKIseCikistarihi = forms.DateField(widget=DatePickerInput)
        PTKEmail = forms.EmailField()
        PTKDosya = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        fields = ["PTKTckimlik","PTKAdiSoyadi","PTKFirmaAdi","PTKIseGiristarihi","PTKIseCikistarihi","PTKHakedilenIzinGun","PTKHakedilenIzinYil","PTKAdres","PTKIlce", "PTKIl","PTKEmail","PTKTelefon","PTKAciklama","PTKDurumu"]


class PTKDuyurularEkleForm(forms.ModelForm):
    class Meta:
        model = PTKDuyurular
        fields = ["PTKDuyuruBaslik", "PTKDuyuruAciklama"]

class UserEkleForm(forms.ModelForm):
    class Meta:
        model = User
        fields =["first_name","last_name"]

class PerTakipNotlarForm(forms.ModelForm):
    class Meta:
        model = PerTakipNotlar
        PerTakipNotDosya = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        fields = ["PerTakipKayit","PerTakipNotlarKonu","PerTakipMetin","PerTakipNotUser"]

class PerTakipNotlarForm(forms.ModelForm):
    class Meta:
        model = PerTakipNotlar
        PerTakipNotDosya = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        fields = ["PerTakipNotlarKonu","PerTakipMetin","PerTakipNotDosya"]

class PerIzinDurumKayitForm(forms.ModelForm):
    class Meta:
        model = PerIzinDurum
        PerIzinDosya = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        fields = ["PerTakipKayit","PerIzinDonemi","PerIzinBaslatarihi","PerIzinBitistarihi","PerIzinKonu","PerIzinSuresiGun","PerIzinSuresiSaat","PerIzinOnayVeren","PerIzinDosya"]
        widgets = {
            'PerIzinBaslatarihi' : DateInput(),
            'PerIzinBitistarihi' : DateInput(),
        }

class PerIzinDurumKayitidForm(forms.ModelForm):
    class Meta:
        model = PerIzinDurum
        PerIzinDosya = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        fields = ["PerIzinDonemi","PerIzinBaslatarihi","PerIzinBitistarihi","PerIzinKonu","PerIzinSuresiGun","PerIzinSuresiSaat","PerIzinOnayVeren","PerIzinDosya"]
        widgets = {
            'PerIzinBaslatarihi' : DateInput(),
            'PerIzinBitistarihi' : DateInput(),
        }
        
class PerIzinDurumForm(forms.ModelForm):
    class Meta:
        model = PerIzinDurum
        PerIzinDosya = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        fields = ["PerTakipKayit","PerIzinDonemi","PerIzinBaslatarihi","PerIzinBitistarihi","PerIzinKonu","PerIzinSuresiGun","PerIzinSuresiSaat","PerIzinOnayVeren","PerIzinDosya"]

