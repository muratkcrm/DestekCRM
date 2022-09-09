from django.shortcuts import render, HttpResponse,redirect, get_object_or_404
from django.contrib import messages
from mongoengine.queryset import query

from Satis.models import SatisGorusmesi, SatisDuyurular, SatisSozlesmeler
from TalepYonetimi.models import Kurumlar, Uygulama
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import PasswordChangeForm
from django.views.decorators.clickjacking import xframe_options_deny,xframe_options_exempt,xframe_options_sameorigin
from .models import SatisGorusmesi, STSsatisNotlar, STSIhaleTakip
from django.core.paginator import Paginator
import logging
from .forms import SatisGorusmesiForm,SatisKurumlarForm, SatisUygulamaEkleForm, SatisDuyuruEkleForm, SatisSozlesmeEkleForm, SatisSozlesmeTakipForm,STSUserEkleForm
from .forms import STSsatisNotlarForm, STSIhaleTakipForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from bs4 import BeautifulSoup, ResultSet
import urllib
from urllib.request import urlopen
import requests


#--------------------- İndex ---------------------

@login_required(login_url="user:login")
def STSindex(request):
    logging.basicConfig(filename='Log/STSindex.log', level=logging.DEBUG)
    pass
    return render(request,"STS/STSindex.html")

#--------------------- Satış Görüşme Takibi ---------------------


@permission_required('Satis.add_satisgorusmesi')
@login_required(login_url="user:login")
def STSgorusmeekle(request):
    logging.basicConfig(filename='Log/STSgorusmeekle.log', level=logging.DEBUG)
    form = SatisGorusmesiForm(request.POST or None)

    if form.is_valid():
        STSgorusmeekle = form.save(commit=False)
        STSgorusmeekle.SatisUser = request.user
        STSgorusmeekle.save()
        messages.success(request, "Kayıt Başarılı.")
        return redirect("/Satis/STSgorusmeekle/")
    return render(request, "STS/STSgorusmeekle.html", {"form": form})


@permission_required('Satis.view_satisgorusmesi')
@login_required(login_url="user:login")
def STSgorusmeler(request):
    logging.basicConfig(filename='Log/STSgorusmeler.log', level=logging.DEBUG)
    Kelime = request.GET.get("Kelime")
    if Kelime:
        STSgorusmelers_listesi = SatisGorusmesi.objects.filter(SatisAktif=True, SatisKonu__contains=Kelime )
    else:
        STSgorusmelers_listesi = SatisGorusmesi.objects.filter(SatisAktif=True)
    paginator = Paginator(STSgorusmelers_listesi, 20 ) # Show 25 contacts per page

    Sayfa = request.GET.get('Sayfa')
    STSgorusmelers = paginator.get_page(Sayfa)
    return render(request, "STS/STSgorusmeler.html", {'STSgorusmelers': STSgorusmelers})

@permission_required('Satis.view_satisgorusmesi')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def STSgorusmedetay(request, id):
    logging.basicConfig(filename='Log/STSgorusmedetay.log', level=logging.DEBUG)
    satisGorusmesi = get_object_or_404(SatisGorusmesi, id=id)
    satisNotlar = STSsatisNotlar.objects.filter(satisGorusmesi=id)
    request.session['SatisDetayID'] = id
    print(satisGorusmesi)
    return render(request, "STS/STSgorusmedetay.html", {"satisGorusmesi": satisGorusmesi,"satisNotlar": satisNotlar})

@permission_required('Satis.change_satisgorusmesi')
@login_required(login_url="user:login")
def STSgorusmeguncelle(request,id):
    logging.basicConfig(filename='Log/STSgorusmeguncelle.log', level=logging.DEBUG)
    #if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    gorusmeler = get_object_or_404(SatisGorusmesi, id=id)
    form = SatisGorusmesiForm(request.POST or None,instance=gorusmeler)
    request.session['gorusmeGuncelleID'] = id
    if form.is_valid():
        STSgorusmeekle = form.save(commit=False)
        STSgorusmeekle.save()
        messages.success(request, "Kayıt Başarıyla Güncellendi...")
    return render(request, "STS/STSgorusmeguncelle.html", {"form": form})

@permission_required('Satis.delete_satisgorusmesi')
@login_required(login_url="user:login")
def STSgorusmesil(request,id):
    logging.basicConfig(filename='Log/STSgorusmesil.log', level=logging.DEBUG)
    #if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    gorusme = get_object_or_404(SatisGorusmesi, id=id)
    gorusme.SatisAktif = False
    gorusme.save()
    messages.info(request, "Kayıt Başarıyla Silindi...")
    return redirect("Satis:STSgorusmeler")

@login_required(login_url="user:login")
def STStekliftakip(request):
    logging.basicConfig(filename='Log/STStekliftalep.log', level=logging.DEBUG)
    pass
    return render(request,"STS/STStekliftakip.html")

@login_required(login_url="user:login")
def STSistatistik(request):
    logging.basicConfig(filename='Log/STSistatistik.log', level=logging.DEBUG)
    pass
    return render(request,"STS/STSistatistik.html")


#--------------------- Sözleşme Takibi ---------------------


@permission_required('Satis.view_satissozlesmetakip')
@login_required(login_url="user:login")
def STSsozlesmetakip(request):
    logging.basicConfig(filename='Log/STSsozlesmetakip.log', level=logging.DEBUG)
    Kelime = request.GET.get("Kelime")
    if Kelime:
        STSsozlesmetakip = SatisSozlesmeler.objects.filter(SozlesmeAktif=True, SozlesmeKonusu__contains=Kelime, SozlesmeDurumu='Devam Eden').order_by('-SozlesmeBitisTarihi')
    else:
        STSsozlesmetakip = SatisSozlesmeler.objects.filter(SozlesmeAktif=True , SozlesmeDurumu='Devam Eden').order_by('-SozlesmeBitisTarihi')
    paginator = Paginator(STSsozlesmetakip, 20 ) # Show 25 contacts per page

    Sayfa = request.GET.get('Sayfa')
    STSsozlesmetakip = paginator.get_page(Sayfa)
    return render(request, "STS/STSsozlesmetakip.html", {"STSsozlesmetakip": STSsozlesmetakip})



@permission_required('Satis.add_satissozlesmetakip')
@login_required(login_url="user:login")
def STSsozlesmetakipekle(request):
    logging.basicConfig(filename='Log/STSsozlesmetakipekle.log', level=logging.DEBUG)
    form = SatisSozlesmeTakipForm(request.POST or None)
    if form.is_valid():
        STSkurumsozlesmeleri = form.save(commit=False)
        STSkurumsozlesmeleri.SatisSozlesmeUser = request.user
        STSkurumsozlesmeleri.save()
        messages.success(request, "Kayıt Başarılı.")
        return redirect("/Satis/STSsozlesmetakipekle/")
    return render(request, "STS/STSsozlesmetakipekle.html", {"form": form})

@permission_required('Satis.view_satissozlesmetakip')
@login_required(login_url="user:login")
def STSsozlesmetakipdetay(request,id):
    logging.basicConfig(filename='Log/STSsozlesmetakipdetay.log', level=logging.DEBUG)
    STSsozlesmetakipdetay = get_object_or_404(SatisSozlesmeler, id=id)
    request.session['sozlesmetakipDetayID'] = id
    return render(request, "STS/STSsozlesmetakipdetay.html", {"STSsozlesmetakipdetay": STSsozlesmetakipdetay})

@permission_required('Satis.change_satissozlesmetakip')
@login_required(login_url="user:login")
def STSsozlesmetakipguncelle(request,id):
    logging.basicConfig(filename='Log/STSsozlesmetakipguncelle.log', level=logging.DEBUG)
    #if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    satistakip = get_object_or_404(SatisSozlesmeler, id=id)
    form = SatisSozlesmeTakipForm(request.POST or None,instance=satistakip)
    request.session['satistakipGuncelleID'] = id
    if form.is_valid():
        STSsozlesmetakipguncelle = form.save(commit=False)
        STSsozlesmetakipguncelle.save()
        messages.success(request, "Kayıt Başarıyla Güncellendi...")
    return render(request, "STS/STSsozlesmetakipguncelle.html", {"form": form})

@permission_required('Satis.delete_satissozlesmetakip')
@login_required(login_url="user:login")
def STSsozlesmetakipsil(request,id):
    logging.basicConfig(filename='Log/STSsozlesmetakipsil.log', level=logging.DEBUG)
    #if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    STSsozlesmetakipsil = get_object_or_404(SatisSozlesmeler, id=id)
    STSsozlesmetakipsil.SatisSozlesmeAktif = False
    STSsozlesmetakipsil.save()
    messages.info(request, "Kayıt Başarıyla Silindi...")
    return redirect("Satis:STSsozlesmetakip")


#--------------------- Sözleşmelerimiz -----------------------

@permission_required('Satis.view_satissozlesmeler')
@login_required(login_url="user:login")
def STSsozlesmelerimiz(request):
    Kelime = request.GET.get("Kelime")
    if Kelime:
        STSsozlesmelerimiz = SatisSozlesmeler.objects.filter(SozlesmeAktif=True, SozlesmeKonusu__contains=Kelime)
    else:
        STSsozlesmelerimiz = SatisSozlesmeler.objects.filter(SozlesmeAktif=True)
    paginator = Paginator(STSsozlesmelerimiz, 20 ) # Show 25 contacts per page
    Sayfa = request.GET.get('Sayfa')
    STSsozlesmelerimiz = paginator.get_page(Sayfa)
    context = {
        "STSsozlesmelerimiz": STSsozlesmelerimiz
    }
    return render(request, "STS/STSsozlesmelerimiz.html", context)


@permission_required('Satis.add_satissozlesmeler')
@login_required(login_url="user:login")
def STSsozlesmeekle(request):
    form = SatisSozlesmeEkleForm(request.POST or None)
    if form.is_valid():
        STSsozlesmeekle = form.save(commit=False)
        STSsozlesmeekle.SatisUser = request.user
        STSsozlesmeekle.save()
        messages.success(request, "Kayıt Başarılı.")
        return redirect("/Satis/STSsozlesmeekle/")
    return render(request, "STS/STSsozlesmeekle.html", {"form": form})

@permission_required('Satis.view_satissozlesmeler')
@login_required(login_url="user:login")
def STSsozlesmedetay(request,id):
    STSsozlesmedetay = get_object_or_404(SatisSozlesmeler, id=id)
    request.session['sozlesmeDetayID'] = id
    return render(request, "STS/STSsozlesmedetay.html", {"STSsozlesmedetay": STSsozlesmedetay})

@permission_required('Satis.change_satissozlesmeler')
@login_required(login_url="user:login")
def STSsozlesmeguncelle(request,id):
    #if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    STSsozlesmeguncelle = get_object_or_404(SatisSozlesmeler, id=id)
    form = SatisSozlesmeEkleForm(request.POST or None,instance=STSsozlesmeguncelle)
    request.session['sozlesmeGuncelleID'] = id
    if form.is_valid():
        STSsozlesmeguncelle = form.save(commit=False)
        STSsozlesmeguncelle.save()
        messages.success(request, "Kayıt Başarıyla Güncellendi...")
    return render(request, "STS/STSsozlesmeguncelle.html", {"form": form})

@permission_required('Satis.delete_satissozlesmeler')
@login_required(login_url="user:login")
def STSsozlesmesil(request,id):
    #if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    STSsozlesmesil = get_object_or_404(SatisSozlesmeler, id=id)
    STSsozlesmesil.SozlesmeAktif= False
    STSsozlesmesil.save()
    messages.info(request, "Kayıt Başarıyla Silindi...")
    return redirect("Satis:STSsozlesmelerimiz")

@permission_required('Satis.view_satissozlesmeler')
@login_required(login_url="user:login")
def STSdevamedensozlesmeler(request):
    Kelime = request.GET.get("Kelime")
    if Kelime:
        STSsozlesmelerimiz = SatisSozlesmeler.objects.filter(SozlesmeAktif=True, SozlesmeDurumu="Devam Eden",  SozlesmeKonusu__contains=Kelime)
    else:
        STSsozlesmelerimiz = SatisSozlesmeler.objects.filter(SozlesmeAktif=True , SozlesmeDurumu="Devam Eden")
    paginator = Paginator(STSsozlesmelerimiz, 20 ) # Show 25 contacts per page

    Sayfa = request.GET.get('Sayfa')
    STSsozlesmelerimiz = paginator.get_page(Sayfa)
    context = {
        "STSsozlesmelerimiz": STSsozlesmelerimiz
    }
    return render(request, "STS/STSsozlesmedevameden.html", context)

@permission_required('Satis.view_satissozlesmeler')
@login_required(login_url="user:login")
def STSbitensozlesmeler(request):
    Kelime = request.GET.get("Kelime")
    if Kelime:
        STSsozlesmelerimiz = SatisSozlesmeler.objects.filter(SozlesmeAktif=True, SozlesmeDurumu="Süresi Biten",  SozlesmeKonusu__contains=Kelime)
    else:
        STSsozlesmelerimiz = SatisSozlesmeler.objects.filter(SozlesmeAktif=True , SozlesmeDurumu="Süresi Biten")
    paginator = Paginator(STSsozlesmelerimiz, 20 ) # Show 25 contacts per page

    Sayfa = request.GET.get('Sayfa')
    STSsozlesmelerimiz = paginator.get_page(Sayfa)
    context = {
        "STSsozlesmelerimiz": STSsozlesmelerimiz
    }
    return render(request, "STS/STSsozlesmebiten.html", context)


#--------------------- Duyuru Tanımları ---------------------

@permission_required('Satis.view_satisduyurular')
@login_required(login_url="user:login")
def STSduyurular(request):
    Duyurulars = SatisDuyurular.objects.filter(DuyuruAktif=True)
    context = {
        "Duyurulars": Duyurulars
    }
    return render(request, "STS/STSduyurular.html", context)

@permission_required('Satis.add_satisduyurular')
@login_required(login_url="user:login")
def STSduyuruekle(request):
    form = SatisDuyuruEkleForm(data=request.POST or None, files=request.FILES or None)
    if form.is_valid():
        STSduyuruekle = form.save(commit=False)
        STSduyuruekle.DuyuruUser = request.user
        STSduyuruekle.save()
        messages.success(request, "Duyuru Başarıyla Yayınlandı.")
        return redirect("/Satis/STSduyuruekle/")
    return render(request, "STS/STSduyuruekle.html", {"form": form})

@permission_required('Satis.view_satisduyurular')
@login_required(login_url="user:login")
def STSduyurudetay(request,id):
    duyurular = get_object_or_404(SatisDuyurular, id=id)
    return render(request, "STS/STSduyurudetay.html", {"duyurular": duyurular})

@permission_required('Satis.change_satisduyurular')
@login_required(login_url="user:login")
def STSduyuruguncelle(request,id):
    Kayits = get_object_or_404(SatisDuyurular, id=id)
    #if request.user != Kayits.DuyuruUser and request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    form = SatisDuyuruEkleForm(request.POST or None, files=request.FILES or None, instance=Kayits)
    request.session['duyuruGuncelleID'] = id
    if form.is_valid():
        STSduyuruekle = form.save(commit=False)
        STSduyuruekle.save()
        messages.success(request, "Kayıt Başarıyla Güncellendi...")
    return render(request, "STS/STSduyuruguncelle.html", {"form": form})

@permission_required('Satis.delete_satisduyurular')
@login_required(login_url="user:login")
def STSduyurusil(request,id):
    #if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    STSduyurusil = get_object_or_404(SatisDuyurular, id=id)
    STSduyurusil.DuyuruAktif = False
    STSduyurusil.save()
    messages.info(request, "Kayıt Başarıyla Silindi...")
    return redirect("Satis:STSduyurular")

#--------------------- Kurum Tanımları ---------------------

@permission_required('Satis.add_satiskurumlar')
@login_required(login_url="user:login")
def STSkurumlarekle(request):
    form = SatisKurumlarForm(request.POST or None)

    if form.is_valid():
        STSkurumlarekle = form.save(commit=False)
        STSkurumlarekle.save()
        messages.success(request, "Kayıt Başarılı.")
        return redirect("/Satis/STSkurumlarekle/")
    return render(request, "STS/STSkurumlarekle.html", {"form": form})

@permission_required('Satis.view_satiskurumlar')
@login_required(login_url="user:login")
def STSkurumlar(request):
    #if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    STSKurumlars = Kurumlar.objects.filter(KurumAktif=True)
    context = {
        "Kurumlars": STSKurumlars
    }
    return render(request, "STS/STSkurumlar.html", context)

@permission_required('Satis.change_satiskurumlar')
@login_required(login_url="user:login")
def STSkurumlarguncelle(request,id):
    #if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    kurumlar = get_object_or_404(Kurumlar, id=id)
    form = SatisKurumlarForm(request.POST or None,request.FILES or None, instance=kurumlar)
    request.session['kurumlarGuncelleID'] = id
    if form.is_valid():
        STSkurumlarekle = form.save(commit=False)
        STSkurumlarekle.save()
        messages.success(request, "Kayıt Başarıyla Güncellendi...")
    return render(request, "STS/STSkurumlarguncelle.html", {"form": form})

@permission_required('Satis.delete_satiskurumlar')
@login_required(login_url="user:login")
def STSkurumlarsil(request,id):
    #if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    kurumlar = get_object_or_404(Kurumlar, id=id)
    kurumlar.KurumAktif = False
    kurumlar.save()
    messages.info(request, "Kayıt Başarıyla Silindi...")
    return redirect("Satis:STSkurumlar")

@permission_required('Satis.view_satiskurumlar')
@login_required(login_url="user:login")
def STSkurumlardetay(request,id):
    kurumlar = get_object_or_404(Kurumlar, id=id)
    return render(request, "STS/STSkurumlardetay.html",{"kurumlar": kurumlar})

#--------------------- Uygulama Tanımları ---------------------

@permission_required('Satis.view_satisuygulama')
@login_required(login_url="user:login")
def STSuygulama(request):
    #if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    Uygulamas = Uygulama.objects.filter(UygulamaAktif=True)
    context = {
        "Uygulamas": Uygulamas
    }
    return render(request, "STS/STSuygulama.html", context)

@permission_required('Satis.add_satisuygulama')
@login_required(login_url="user:login")
def STSuygulamaekle(request):
    #if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    form = SatisUygulamaEkleForm(request.POST or None)
    if form.is_valid():
        STSuygulamaekle = form.save(commit=False)
        STSuygulamaekle.save()
        messages.success(request, "Kayıt Girişi Yapıldı.")
        return redirect("/Satis/STSuygulamaekle/")
    return render(request, "STS/STSuygulamaekle.html", {"form": form})

@permission_required('Satis.change_satisuygulama')
@login_required(login_url="user:login")
def STSuygulamaguncelle(request,id):
    #if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    uygulama = get_object_or_404(Uygulama, id=id)
    form = SatisUygulamaEkleForm(request.POST or None,request.FILES or None, instance=uygulama)
    request.session['uygulamaGuncelleID1'] = id
    if form.is_valid():
        STSuygulamaguncelle = form.save(commit=False)
        STSuygulamaguncelle.save()
        messages.success(request, "Kayıt Başarıyla Güncellendi...")
        return redirect("Satis:STSuygulama")
    return render(request, "STS/STSuygulamaguncelle.html", {"form": form})

@permission_required('Satis.delete_satisuygulama')
@login_required(login_url="user:login")
def STSuygulamasil(request,id):
    #if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    uygulama = get_object_or_404(Uygulama, id=id)
    uygulama.UygulamaAktif = False
    uygulama.save()
    messages.info(request, "Kayıt Başarıyla Silindi...")
    return redirect("Satis:STSuygulama")

# ------------------ profil güncelleme------------

@login_required(login_url="user:login")
def STSUserprofil(request):
    if request.method == 'POST':
        form = STSUserEkleForm(data=request.POST, instance=request.user)
        update = form.save(commit=False)
        update.user = request.user
        update.save()
        messages.success(request, "Başarıyla Günceleme Yaptınız...")
    else:
        form = STSUserEkleForm(instance=request.user)
        messages.info(request, "Günceleme Yapılmadı...")
    return render(request,"STS/Userprofil.html", {"form" : form})

def STSUserPasswordChange(request):
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
    return render(request, 'STS/UserPasswordChange.html', {'form': form })


# --------------- Satiş Not İşlemleri --------------


@xframe_options_sameorigin
@login_required(login_url="user:login")
def satisNotGuncelle(request, id):
    pass

@permission_required('Satis.add_stssatisnotlar')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def satisNotEkle(request,id):
    logging.basicConfig(filename='Log/satisNotEkle.log', level=logging.DEBUG)
    request.session['SatisDetayID'] = id
    form = STSsatisNotlarForm(data=request.POST or None, files=request.FILES or None)
    kayits = get_object_or_404(SatisGorusmesi, id=id)
    if form.is_valid():
        NewNotEkle = form.save(commit=False)
        NewNotEkle.satisNotUser = request.user
        NewNotEkle.satisGorusmesi = kayits
        NewNotEkle.save()
        messages.success(request, "Not Başarıyla Kayıt Edildi..")
    return render(request, "STS/STSsatisNotEkle.html", {"form": form})

@permission_required('Satis.view_stssatisnotlar')
@login_required(login_url="user:login")
def satisNotDetay(request, id):
    logging.basicConfig(filename='Log/satisNotDetay.log', level=logging.DEBUG)
    satisGorusmesi1 = get_object_or_404(SatisGorusmesi, id=id)
    STSsatisNotlars = STSsatisNotlar.objects.filter(SatisAktif=True)
    request.session['kayitGuncelleID'] = id
    return render(request, "Satis/STSgorusmedetay/.html", {"STSsatisNotlars": STSsatisNotlars,"satisGorusmesil": satisGorusmesi1 })

@permission_required('Satis.delete_stssatisnotlar')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def satisNotSil(request, id):
    logging.basicConfig(filename='Log/satisNotSil.log', level=logging.DEBUG)
    kayits = get_object_or_404(STSsatisNotlar, id=id)
    kayits.satisNotAktif=False
    kayits.save()
    messages.info(request, "Kayıt Başarıyla Silindi...")
    return redirect("Satis:STSgorusmedetay")

@xframe_options_sameorigin
@login_required(login_url="user:login")
def STSindex(request):
    logging.basicConfig(filename='Log/STSindex.log', level=logging.DEBUG)

    Duyurulars = SatisDuyurular.objects.filter(DuyuruAktif=True)
    CagriKayits = SatisGorusmesi.objects.filter(SatisAktif=True)
    Sozlesmelers = SatisSozlesmeler.objects.filter(SozlesmeDurumu="Devam Eden")[:5][::-1]
    SozlesmeTakips = SatisSozlesmeler.objects.filter(SozlesmeAktif=True)[:5][::-1]

    form=SatisGorusmesi.objects.filter()
    Cagrisayisi=len(form)
    request.session['Cagrisayisissts'] = Cagrisayisi

    formUserSayi=User.objects.filter(is_active=True)
    UserSayi=len(formUserSayi)
    request.session["UserSayisi"] = UserSayi

    formKurumSayisi=Kurumlar.objects.filter(KurumAktif=True)
    KurumSayisi=len(formKurumSayisi)
    request.session["KurumSayisis"] = KurumSayisi

    return render(request,"STS/STSindex.html",{'Duyurulars':Duyurulars, "CagriKayits": CagriKayits,
                                               "Sozlesmelers":Sozlesmelers,"SozlesmeTakips":SozlesmeTakips})



# ---------------------- kurum ihalelerinin çekilmesi ---------------------------

@permission_required('Satis.view_STSihaletakip')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def STSihaletakip(request):
    if request.user.is_superuser != True:
        return HttpResponseForbidden()
    Uygulamas = STSIhaleTakip.objects.filter(IhaleAktif=True)
    return render(request, "STS/STSihaletakip.html", {"Uygulamas":Uygulamas})