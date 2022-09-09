from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User





# ----------------- kullanıcı Ekleme İşlemleri --------------------------------

class YONregisterEkleForm(forms.ModelForm):
    username = forms.CharField(max_length=100,label="Kullanıcı Adı",widget=forms.TextInput(attrs={'class' : 'form-control'}),required=True)
    password = forms.CharField(max_length=10,label="Parolası",widget=forms.PasswordInput(attrs={'class' : 'form-control'}),required=True)
    confirm = forms.CharField(max_length=10,label="Parolayı Tekrar Yazınız",widget=forms.PasswordInput(attrs={'class' : 'form-control'}),required=True)
    first_name = forms.CharField(max_length=100,label="Adı",widget=forms.TextInput(attrs={'class' : 'form-control'}),required=True)
    last_name = forms.CharField(max_length=100,label="Soyadı",widget=forms.TextInput(attrs={'class' : 'form-control'}),required=True)
    email = forms.CharField(max_length=100,label="E-mail",widget=forms.TextInput(attrs={'class' : 'form-control'}),required=False)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')

        if password and confirm and password!=confirm:
            raise forms.ValidationError('Parola Eşleşme Hatası')

        values = {
            "username" : username,
            "password" : password,
            "first_name" : first_name,
            "last_name" : last_name,
            "email" : email
        }
        return values


    class Meta:
        model = User
        fields = ['username','password','confirm','first_name','last_name','email']



# ----------------- kullanıcı Güncelleme İşlemleri --------------------------------

class YONregisterGuncelleForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','is_active']


#----------------- Kullanıcı Şifre Güncelleme -------------------------------------

class YONregisterSifreForm(forms.ModelForm):
    password = forms.CharField(max_length=10, label="Parolası",
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
    confirm = forms.CharField(max_length=10, label="Parolayı Tekrar Yazınız",
                              widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)


    def clean(self):
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')

        if password and confirm and password != confirm:
            raise forms.ValidationError('Parola Eşleşme Hatası')

        values = {
            "password": password,

        }
        return values

    class Meta:
        model = User
        fields = ['password']

