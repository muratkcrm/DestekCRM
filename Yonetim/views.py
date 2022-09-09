from django.shortcuts import render, HttpResponse,redirect, get_object_or_404
from django.contrib import messages

from PerTakip.models import PerTakipKayit
from TalepYonetimi.models import  DestekTalebiTuru, Kategori, Uygulama, Kurumlar, KurumBirimi,Kisi
from TalepYonetimi.models import  Uygulama, Kurumlar
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from .forms import YONregisterEkleForm, YONregisterGuncelleForm,YONregisterSifreForm
from django.contrib.auth import authenticate
from django.views.decorators.clickjacking import xframe_options_deny,xframe_options_exempt,xframe_options_sameorigin
import logging
from django.contrib.auth.decorators import permission_required


@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONindex(request):
    return render(request,"YON/YONindex.html")

#------------------ kurumlar ----------------

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONkurumlarGuncelle(request, id):
    if request.user.is_superuser != True:
        return HttpResponseForbidden()
    kurumlar = get_object_or_404(Kurumlar, id=id)
    kurumlar.KurumAktif = True
    kurumlar.save()
    messages.info(request, "Silme İşlemi Geri Alındı....")
    return redirect("Yonetim:YONkurumlar")

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONkurumlar(request):
    Kurumlars = Kurumlar.objects.filter(KurumAktif=False)
    context = {
        "Kurumlars": Kurumlars
    }
    return render(request,"YON/YONkurumlar.html",context)

#------------------------kurumBirimi -------------------

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONkurumBirimiGuncelle(request, id):
    if request.user.is_superuser != True:
        return HttpResponseForbidden()
    kurumlar = get_object_or_404(KurumBirimi, id=id)
    kurumlar.BirimAktif = True
    kurumlar.save()
    messages.info(request, "Silme İşlemi Geri Alındı....")
    return redirect("Yonetim:YONkurumBirimi")

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONkurumBirimi(request):
    KurumBirimis = KurumBirimi.objects.filter(BirimAktif=False)
    context = {
        "KurumBirimis": KurumBirimis
    }
    return render(request,"YON/YONkurumBirimi.html",context)

#------------------------Personel kayıt takip -------------------

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONPertakipGuncelle(request, id):
    if request.user.is_superuser != True:
        return HttpResponseForbidden()
    PersonelKayit = get_object_or_404(PerTakipKayit, id=id)
    PersonelKayit.PTKAktif = True
    PersonelKayit.save()
    messages.info(request, "Silme İşlemi Geri Alındı....")
    return redirect("Yonetim:YONPertakip")

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONPertakip(request):
    PersonelKayit = PerTakipKayit.objects.filter(PTKAktif=False)
    context = {
        "PersonelKayits": PersonelKayit
    }
    return render(request,"YON/YONPertakip.html",context)

#--------------------Uygulama -----------------------------

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONuygulamaGuncelle(request, id):
    if request.user.is_superuser != True:
        return HttpResponseForbidden()
    uygulama = get_object_or_404(Uygulama, id=id)
    uygulama.UygulamaAktif = True
    uygulama.save()
    messages.info(request, "Silme İşlemi Geri Alındı....")
    return redirect("Yonetim:YONuygulama")

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONuygulama(request):
    Uygulamas = Uygulama.objects.filter(UygulamaAktif=False)
    context = {
        "Uygulamas": Uygulamas
    }
    return render(request,"YON/YONuygulama.html",context)

#--------------------destekTalebi -------------------------

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONdestekTalebiTuruGuncelle(request, id):
    if request.user.is_superuser != True:
        return HttpResponseForbidden()
    uygulama = get_object_or_404(DestekTalebiTuru, id=id)
    uygulama.DestekTalebiAktif = True
    uygulama.save()
    messages.info(request, "Silme İşlemi Geri Alındı....")
    return redirect("Yonetim:YONdestekTalebiTuru")

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONdestekTalebiTuru(request):
    destekTalebis = DestekTalebiTuru.objects.filter(DestekTalebiAktif=False)
    context = {
        "destekTalebis": destekTalebis
    }
    return render(request,"YON/YONdestekTalebiTuru.html",context)

#--------------------kategori -----------------------------

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONkategoriGuncelle(request, id):
    if request.user.is_superuser != True:
        return HttpResponseForbidden()
    uygulama = get_object_or_404(Kategori, id=id)
    uygulama.KategoriAktif = True
    uygulama.save()
    messages.info(request, "Silme İşlemi Geri Alındı....")
    return redirect("Yonetim:YONkategori")

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONkategori(request):
    Kategoris = Kategori.objects.filter(KategoriAktif=False)
    context = {
        "Kategoris": Kategoris
    }
    return render(request,"YON/YONkategori.html", context)

#--------------------kisi ---------------------------------

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONkisiGuncelle(request, id):
    if request.user.is_superuser != True:
        return HttpResponseForbidden()
    uygulama = get_object_or_404(Kisi, id=id)
    uygulama.KisiAktif = True
    uygulama.save()
    messages.info(request, "Silme İşlemi Geri Alındı....")
    return redirect("Yonetim:YONkisi")


@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONkisi(request):
    kisis = Kisi.objects.filter(KisiAktif=False)
    context = {
        "kisis": kisis
    }
    return render(request,"YON/YONkisi.html",context)

#--------------------Satış Uygulama -----------------------------

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONstsuygulamaGuncelle(request, id):
    if request.user.is_superuser != True:
        return HttpResponseForbidden()
    Uygulamas = get_object_or_404(Uygulama, id=id)
    Uygulamas.UygulamaAktif = True
    Uygulamas.save()
    messages.info(request, "Silme İşlemi Geri Alındı....")
    return redirect("Yonetim:YONstsuygulama")

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONstsuygulama(request):
    Uygulamas = Uygulama.objects.filter(UygulamaAktif = False)
    context = {
        "Uygulamas": Uygulamas
    }
    return render(request,"YON/YONstsuygulama.html",context)

#------------------ Satış kurumlar ----------------

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONstskurumlarGuncelle(request, id):
    if request.user.is_superuser != True:
        return HttpResponseForbidden()
    kurumlar = get_object_or_404(Kurumlar, id=id)
    kurumlar.KurumAktif = True
    kurumlar.save()
    messages.info(request, "Silme İşlemi Geri Alındı....")
    return redirect("Yonetim:YONstskurumlar")

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONstskurumlar(request):
    Kurumlars = Kurumlar.objects.filter(KurumAktif=False)
    context = {
        "Kurumlars": Kurumlars
    }
    return render(request,"YON/YONstskurumlar.html",context)

#------------------------ Şifre Değiştirme -----------------

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONUserPasswordChange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, '"Parola Değişimi Yapıldı...."!')
        else:
            messages.info(request, "Parola Değişmedi...")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'YON/UserPasswordChange.html', {'form': form})

# ---------------------- Genel Kullanıcı Şifre Güncelleme -----------------

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONregisterSifre(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, '"Parola Değişimi Yapıldı...."!')
        else:
            messages.info(request, "Parola Değişmedi...")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'YON/UserPasswordChange.html', {'form': form})



#-----------------------Kullanıcı Oluşturma ----------------
@permission_required('Yonetim.view_user')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONregister(request):
    formuser1 = User.objects.filter()
    context = {
        "formuser1": formuser1
    }
    return render(request,"YON/YONregister.html",context)


#------------------- Kullanıcı Guncelleme ----------------------

@permission_required('Yonetim.change_user')
@login_required(login_url="user:login")
def YONregisterGuncelle(request,id):
    #if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    profile = get_object_or_404(User, id=id)
    form = YONregisterGuncelleForm(data=request.POST or None, files=request.FILES or None, instance=profile)
    if form.is_valid():
        newUser = form.save(commit=False)
        newUser.save()
        messages.success(request, "Kullanıcı Kaydı Yapıldı....")
        return  redirect("Yonetim:YONregister")
    return render(request,"YON/YONregisterEkle.html", {"form": form})


#------------------- Kullanıcı Ekleme ----------------------

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONregisterEkle(request):
    if request.user.is_superuser != True:
        return HttpResponseForbidden()
    form = YONregisterEkleForm(data=request.POST or None, files=request.FILES or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        email = form.cleaned_data.get("email")

        newUser = User(username=username,
                       first_name=first_name,
                       last_name=last_name,
                       email=email)

        newUser.set_password(password)
        newUser.save()

        messages.success(request, "Kullanıcı Kaydı Yapıldı....")
        return  redirect("Yonetim:YONregister")
    return render(request,"YON/YONregisterEkle.html", {"form": form})


#-----------------kullanıcı Şifre işlemleri

@permission_required('Yonetim.add_user')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONKullaniciSifre(request,id):
    #if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    profile = get_object_or_404(User, id=id)
    form = YONregisterSifreForm(data=request.POST or None, files=request.FILES or None, instance=profile)
    request.session['YONadi'] = profile.first_name
    request.session['YONSoyadi'] = profile.last_name
    request.session['YONemail'] = profile.email
    request.session['YONusers'] = profile.username

    if form.is_valid():
        newUser = form.save(commit=False)
        password = form.cleaned_data.get("password")
        newUser.set_password(password)
        newUser.save()
        messages.success(request, "Şifre Güncellendi.....")
        return  redirect("Yonetim:YONregister")
    return render(request,"YON/UserparolarReset.html", {"form": form})

#--------------------Cari Hesap Uygulama -----------------------------

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONonmcarihesapGuncelle(request, id):
    if request.user.is_superuser != True:
        return HttpResponseForbidden()
    CariHesaps = get_object_or_404(ONMCariKayit, id=id)
    CariHesaps.CariAktif = True
    CariHesaps.save()
    messages.info(request, "Silme İşlemi Geri Alındı....")
    return redirect("Yonetim:YONonmcarihesap")

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONonmcarihesap(request):
    CariHesaps = ONMCariKayit.objects.filter(CariAktif = False)
    context = {
        "CariHesaps": CariHesaps
    }
    return render(request,"YON/YONonmcarihesap.html",context)

#--------------------Hesap Planı Uygulama -----------------------------

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONonmhesapplaniGuncelle(request, id):
    if request.user.is_superuser != True:
        return HttpResponseForbidden()
    HesapPlanis = get_object_or_404(ONMHesapPlani, id=id)
    HesapPlanis.HesapAktif = True
    HesapPlanis.save()
    messages.info(request, "Silme İşlemi Geri Alındı....")
    return redirect("Yonetim:YONonmhesapplani")

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONonmhesapplani(request):
    HesapPlanis = ONMHesapPlani.objects.filter(HesapAktif = False)
    context = {
        "HesapPlanis": HesapPlanis
    }
    return render(request,"YON/YONonmhesapplani.html",context)

#--------------------Stok Kartı Uygulama -----------------------------

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONonmstokkartGuncelle(request, id):
    if request.user.is_superuser != True:
        return HttpResponseForbidden()
    StokKarts = get_object_or_404(ONMStokKart, id=id)
    StokKarts.StokAktif = True
    StokKarts.save()
    messages.info(request, "Silme İşlemi Geri Alındı....")
    return redirect("Yonetim:YONonmstokkart")

@xframe_options_sameorigin
@login_required(login_url="user:login")
def YONonmstokkart(request):
    StokKarts = ONMStokKart.objects.filter(StokAktif = False)
    context = {
        "StokKarts": StokKarts
    }
    return render(request,"YON/YONonmstokkart.html",context)