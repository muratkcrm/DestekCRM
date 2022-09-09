from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
#from captcha.fields import ReCaptchaField

class LoginForm(forms.Form):

    username = forms.CharField(required=True, max_length=50, label = "Kullanıcı Adı",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True, max_length=50, label = "Parola",
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    #captcha=ReCaptchaField()

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password= password)
        if not user:
            raise forms.ValidationError('Hatalı Kullanıcı Adı veya şifre girdiniz..')



        
class UserEkleForm(forms.ModelForm):
    class Meta:
        model = User
        fields =["first_name","last_name","email"]