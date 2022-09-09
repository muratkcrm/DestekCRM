from itertools import count
import logging
from pickle import NONE
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import PasswordChangeForm
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.clickjacking import xframe_options_sameorigin
from pymysql import NULL
from PerTakip.Hesaplama import HesaplamaIzinYil, HesaplamaIzinGun, HesaplamaIzinYilAyrilan, HesaplamaIzinGunAyrılan
from PerTakip.models import PTKDuyurular, PerIzinDurum
from .forms import PerIzinDurumKayitForm, PerIzinDurumKayitidForm, PerTakipKayitForm, PTKDuyurularEkleForm, UserEkleForm, PerTakipNotlarForm,PerIzinDurumForm, PerTakipKayitEklemeForm
from .models import PerTakipKayit, PTKDuyurular, PerTakipNotlar, PTKFirma, PerIzinHakedis
from django.db.models import Q, Sum
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
import csv
import xlwt
import logging



# Create your views here.

# ------------------  PTK İndex ---------------
@login_required(login_url="user:login")
def PTKindex(request):
    logging.basicConfig(filename='Log/PTKindex.log', level=logging.DEBUG)
    PersonelKayits = PerTakipKayit.objects.filter(PTKAktif__in=[True])
    Duyurulars = PTKDuyurular.objects.filter(PTKDuyuruAktif__in=[True])

    formAktif=PerTakipKayit.objects.filter(PTKDurumu__in=['Çalışıyor'])
    PersonelsayisiAktif=len(formAktif)
    request.session['PersonelsayisiAktifs'] = PersonelsayisiAktif

    formfalse=PerTakipKayit.objects.filter(PTKDurumu__in=['Ayrıldı'])
    PersonelsayisiPasif=len(formfalse)
    request.session['PersonelsayisiPasifs'] = PersonelsayisiPasif

    return render(request, "PTK/PTKindex.html", {'Duyurulars': Duyurulars, "PersonelKayits": PersonelKayits})


# ------------------ PTK Defteri işlemleri ---------------

@permission_required('PerTakip.view_pertakipkayit')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKkayitacik(request):
    logging.basicConfig(filename='Log/PTKkayitdebug.log', level=logging.DEBUG)
    Kelime = request.GET.get("Kelime")
    print(Kelime)
    if Kelime:
        PTKDefteriKayit_listesi = PerTakipKayit.objects.filter(Q(PTKAktif__in=[True]) & Q(PTKTckimlik__contains=Kelime) | Q(PTKAdiSoyadi__icontains=Kelime) | Q(PTKAdres__icontains=Kelime) | Q(PTKIl__icontains=Kelime) |Q(PTKAciklama__icontains=Kelime) & Q(PTKDurumu__in="Çalışıyor"))
        print(" kelime var arama çalışanlarda yapılıyor.", Kelime, PTKDefteriKayit_listesi)
    else:
        PTKDefteriKayit_listesi = PerTakipKayit.objects.filter(PTKAktif__in=[True], PTKDurumu__in=["Çalışıyor"])
    paginator = Paginator(PTKDefteriKayit_listesi, 20 ) # Show 25 contacts per page

    Sayfa = request.GET.get('Sayfa')
    PersonelKayits = paginator.get_page(Sayfa)
    print()
    return render(request, "PTK/PTKkayitacik.html", {'PersonelKayits': PersonelKayits})

@permission_required('PerTakip.view_pertakipkayit')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKkayitacikizindurum(request):
    logging.basicConfig(filename='Log/PTKkayitdebug.log', level=logging.DEBUG)
    Kelime = request.GET.get("Kelime")
    print(Kelime)
    if Kelime:
        PTKDefteriKayit_listesi = PerTakipKayit.objects.filter(Q(PTKAktif__in=[True]) & Q(PTKTckimlik__contains=Kelime) | Q(PTKAdiSoyadi__icontains=Kelime) | Q(PTKAdres__icontains=Kelime) | Q(PTKIl__icontains=Kelime) |Q(PTKAciklama__icontains=Kelime) & Q(PTKDurumu__in="Çalışıyor"))
        print(" kelime var arama çalışanlarda yapılıyor.", Kelime, PTKDefteriKayit_listesi)
    else:
        PTKDefteriKayit_listesi = PerTakipKayit.objects.filter(PTKAktif__in=[True], PTKDurumu__in=["Çalışıyor"])
    paginator = Paginator(PTKDefteriKayit_listesi, 20 ) # Show 25 contacts per page

    Sayfa = request.GET.get('Sayfa')
    PersonelKayits = paginator.get_page(Sayfa)
    print()
    return render(request, "PTK/PTKkayitacikizindurum.html", {'PersonelKayits': PersonelKayits})




@permission_required('PerTakip.view_pertakipkayit')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKkayitkapali(request):
    logging.basicConfig(filename='Log/PTKkayitdebug.log', level=logging.DEBUG)
    Kelime = request.GET.get("Kelime")
    if Kelime:
        PTKDefteriKayit_listesi = PerTakipKayit.objects.filter(Q(PTKAktif__in=[True]) & Q(PTKTckimlik__contains=Kelime) | Q(PTKAdiSoyadi__icontains=Kelime) | Q(PTKAdres__icontains=Kelime) | Q(PTKIl__icontains=Kelime) |Q(PTKAciklama__icontains=Kelime) & Q(PTKDurumu__in="Ayrıldı"))
        print(" kelime var arama ayrılanlar yapılıyor.", Kelime, PTKDefteriKayit_listesi)
    else:
        PersonelKayit_listesi = PerTakipKayit.objects.filter(PTKAktif__in=[True], PTKDurumu__in=["Ayrıldı"])
    paginator = Paginator(PersonelKayit_listesi, 20 ) # Show 25 contacts per page

    Sayfa = request.GET.get('Sayfa')
    PersonelKayits = paginator.get_page(Sayfa)
    return render(request, "PTK/PTKkayitkapali.html", {'PersonelKayits': PersonelKayits})

@permission_required('PerTakip.view_pertakipkayit')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKkayitkapaliizindurum(request):
    logging.basicConfig(filename='Log/PTKkayitdebug.log', level=logging.DEBUG)
    Kelime = request.GET.get("Kelime")
    if Kelime:
        PTKDefteriKayit_listesi = PerTakipKayit.objects.filter(Q(PTKAktif__in=[True]) & Q(PTKTckimlik__contains=Kelime) | Q(PTKAdiSoyadi__icontains=Kelime) | Q(PTKAdres__icontains=Kelime) | Q(PTKIl__icontains=Kelime) |Q(PTKAciklama__icontains=Kelime) & Q(PTKDurumu__in="Ayrıldı"))
        print(" kelime var arama ayrılanlar yapılıyor.", Kelime, PTKDefteriKayit_listesi)
    else:
        PersonelKayit_listesi = PerTakipKayit.objects.filter(PTKAktif__in=[True], PTKDurumu__in=["Ayrıldı"])
    paginator = Paginator(PersonelKayit_listesi, 20 ) # Show 25 contacts per page

    Sayfa = request.GET.get('Sayfa')
    PersonelKayits = paginator.get_page(Sayfa)
    return render(request, "PTK/PTKkayitkapaliizindurum.html", {'PersonelKayits': PersonelKayits})


@permission_required('PerTakip.add_pertakipkayit')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKkayitEkle(request):
    logging.basicConfig(filename='Log/kayitdebug.log', level=logging.DEBUG)
    form = PerTakipKayitEklemeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        kayitEkle = form.save(commit=False)
        print(kayitEkle.PTKIseCikistarihi)      
        if kayitEkle.PTKDurumu == 'Ayrıldı':
            kayitEkle.PTKHakedilenIzinYil = HesaplamaIzinYilAyrilan(kayitEkle.PTKIseGiristarihi, kayitEkle.PTKIseCikistarihi  )
            kayitEkle.PTKHakedilenIzin = HesaplamaIzinGunAyrılan(kayitEkle.PTKIseGiristarihi, kayitEkle.PTKIseCikistarihi  )
        else :
            kayitEkle.PTKHakedilenIzinYil = HesaplamaIzinYil(kayitEkle.PTKIseGiristarihi)
            kayitEkle.PTKHakedilenIzin = HesaplamaIzinGun(kayitEkle.PTKIseGiristarihi)
        kayitEkle.save()
        messages.success(request, "Kayıt Girişi Yapıldı.")
        return redirect("/PerTakip/PTKkayitEkle/")
    return render(request, "PTK/PTKkayitEkleme.html", {"form": form})

@permission_required('PerTakip.change_pertakipkayit')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKkayitGuncelle(request, id):
    logging.basicConfig(filename='Log/PTKkayitGuncelledebug.log', level=logging.DEBUG)
    Kayits = get_object_or_404(PerTakipKayit, id=id)
    #if request.user != Kayits.PTKKayitUser and request.user.is_superuser != True:
    #    return HttpResponseForbidden(" Yetkiniz Yoktur.!!!")
    request.session['kayitGuncelleID'] = id
    form = PerTakipKayitForm(request.POST or None, request.FILES or None, instance=Kayits)
    PersonelKullanilanizinGun = PerIzinDurum.objects.filter(PerTakipKayit__in=[id]).aggregate(Sum(('PerIzinSuresiGun')))['PerIzinSuresiGun__sum']
    PersonelKullanilanizinSaat = PerIzinDurum.objects.filter(PerTakipKayit__in=[id]).aggregate(Sum(('PerIzinSuresiSaat')))['PerIzinSuresiSaat__sum']
    if form.is_valid():
        kayitEkle = form.save(commit=False)
        if kayitEkle.PTKDurumu == 'Ayrıldı':
            kayitEkle.PTKHakedilenIzinYil = HesaplamaIzinYilAyrilan(kayitEkle.PTKIseGiristarihi, kayitEkle.PTKIseCikistarihi  )
            kayitEkle.PTKHakedilenIzinGun = HesaplamaIzinGunAyrılan(kayitEkle.PTKIseGiristarihi, kayitEkle.PTKIseCikistarihi  )
            if kayitEkle.PTKHakedilenIzinGun == None:
                kayitEkle.PTKkalanizin = -PersonelKullanilanizinGun
            elif PersonelKullanilanizinGun == None:
                kayitEkle.PTKkalanizin = kayitEkle.PTKHakedilenIzinGun
            elif PersonelKullanilanizinGun == None or kayitEkle.PTKHakedilenIzinGun == None:
                kayitEkle.PTKkalanizin = 0
            else :
                kayitEkle.PTKkalanizin = kayitEkle.PTKHakedilenIzinGun - PersonelKullanilanizinGun
            
            if kayitEkle.PTKIzinSuresiGun == None:
                kayitEkle.PTKIzinSuresiGun = 0
            else :
                kayitEkle.PTKIzinSuresiGun = PersonelKullanilanizinGun
            
            if kayitEkle.PTKIzinSuresiSaat == None:
                kayitEkle.PTKIzinSuresiSaat = 0
            else :
                kayitEkle.PTKIzinSuresiSaat = PersonelKullanilanizinSaat
                    
        else :
            kayitEkle.PTKHakedilenIzinYil = HesaplamaIzinYil(kayitEkle.PTKIseGiristarihi)
            kayitEkle.PTKHakedilenIzinGun = HesaplamaIzinGun(kayitEkle.PTKIseGiristarihi)
            if kayitEkle.PTKHakedilenIzinGun == None:
                kayitEkle.PTKkalanizin = -PersonelKullanilanizinGun
            elif PersonelKullanilanizinGun == None:
                kayitEkle.PTKkalanizin = kayitEkle.PTKHakedilenIzinGun
            elif PersonelKullanilanizinGun == None or kayitEkle.PTKHakedilenIzinGun == None:
                kayitEkle.PTKkalanizin = 0
            else :
                kayitEkle.PTKkalanizin = kayitEkle.PTKHakedilenIzinGun - PersonelKullanilanizinGun
                
            if kayitEkle.PTKIzinSuresiGun == None:
                kayitEkle.PTKIzinSuresiGun = 0
            else :
                kayitEkle.PTKIzinSuresiGun = PersonelKullanilanizinGun
                
            if kayitEkle.PTKIzinSuresiSaat == None:
                kayitEkle.PTKIzinSuresiSaat = 0
            else :
                kayitEkle.PTKIzinSuresiSaat = PersonelKullanilanizinSaat
        kayitEkle.save()
    messages.success(request, "Kayıt Başarıyla Güncellendi...")
    return render(request, "PTK/PTKkayitGuncelleme.html", {"form": form})


@permission_required('PerTakip.delete_pertakipkayit')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKkayitSil(request, id):
    logging.basicConfig(filename='Log/PTKkayitSildebug.log', level=logging.DEBUG)
    kayits = get_object_or_404(PerTakipKayit, id=id)
    if request.user != kayits.PTKKayitUser and request.user.is_superuser != True:
        return HttpResponseForbidden()
    request.session['kayitGuncelleID'] = id
    kayits.PTKAktif = False
    kayits.save()
    messages.info(request, "Kayıt Başarıyla Silindi...")
    return redirect("PerTakip:PTKkayitacik")

@permission_required('PerTakip.view_pertakipkayit')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKkayitDetay(request, id):
    logging.basicConfig(filename='Log/PTKkayitdebug.log', level=logging.DEBUG)
    PersonelKayit = get_object_or_404(PerTakipKayit, id=id)
    PersonelKayitNot = PerTakipNotlar.objects.filter(PerTakipKayit__in=[id])
    PersonelKayitizin = PerIzinDurum.objects.filter(PerTakipKayit__in=[id])
    request.session['kayitDetayID'] = id
    return render(request, "PTK/PTKkayitDetay.html", {"PersonelKayit": PersonelKayit,"PersonelKayitNot": PersonelKayitNot,
                                                      "PersonelKayitizin": PersonelKayitizin})
    
@permission_required('PerTakip.view_pertakipkayit')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKkayitizinDetay(request, id):
    logging.basicConfig(filename='Log/PTKkayitdebug.log', level=logging.DEBUG)
    PersonelKayit = get_object_or_404(PerTakipKayit, id=id)
    PersonelKayitizin = PerIzinDurum.objects.filter(PerTakipKayit__in=[id])
    PersonelKullanilanizinGun = PerIzinDurum.objects.filter(PerTakipKayit__in=[id]).aggregate(Sum(('PerIzinSuresiGun')))['PerIzinSuresiGun__sum']
    PersonelKullanilanizinSaat = PerIzinDurum.objects.filter(PerTakipKayit__in=[id]).aggregate(Sum(('PerIzinSuresiSaat')))['PerIzinSuresiSaat__sum']
    print(PersonelKullanilanizinGun, PersonelKullanilanizinSaat)
    request.session['kayitDetayID'] = id
    return render(request, "PTK/PTKkayitizinDetay.html",  {"PersonelKayit": PersonelKayit,"PersonelKayitizin": PersonelKayitizin})

# ------------------ PTK hakedilen izinleri Hesaplama
@permission_required('PerTakip.change_pertakipkayit')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKkayitHesaplama(request, id):
    logging.basicConfig(filename='Log/PTKkayithesapladebug.log', level=logging.DEBUG)
    Kayits = get_object_or_404(PerTakipKayit, id=id)
    request.session['kayitGuncelleID'] = id
    form = PerTakipKayitForm(request.POST or None, request.FILES or None, instance=Kayits)
    PersonelKullanilanizinGun = PerIzinDurum.objects.filter(PerTakipKayit__in=[id]).aggregate(Sum(('PerIzinSuresiGun')))['PerIzinSuresiGun__sum']
    PersonelKullanilanizinSaat = PerIzinDurum.objects.filter(PerTakipKayit__in=[id]).aggregate(Sum(('PerIzinSuresiSaat')))['PerIzinSuresiSaat__sum']
    print(PersonelKullanilanizinGun, PersonelKullanilanizinSaat)
    #print(form)
    kayitEkle = form.save(commit=False)
    

    if kayitEkle.PTKDurumu == 'Ayrıldı':
        kayitEkle.PTKHakedilenIzinYil = HesaplamaIzinYilAyrilan(kayitEkle.PTKIseGiristarihi, kayitEkle.PTKIseCikistarihi  )
        kayitEkle.PTKHakedilenIzinGun = HesaplamaIzinGunAyrılan(kayitEkle.PTKIseGiristarihi, kayitEkle.PTKIseCikistarihi  )
        if kayitEkle.PTKHakedilenIzinGun == None:
            kayitEkle.PTKkalanizin = -PersonelKullanilanizinGun
        elif PersonelKullanilanizinGun == None:
            kayitEkle.PTKkalanizin = kayitEkle.PTKHakedilenIzinGun
        elif PersonelKullanilanizinGun == None or kayitEkle.PTKHakedilenIzinGun == None:
            kayitEkle.PTKkalanizin = 0
        else :
            kayitEkle.PTKkalanizin = kayitEkle.PTKHakedilenIzinGun - PersonelKullanilanizinGun
        
        if kayitEkle.PTKIzinSuresiGun == None:
            kayitEkle.PTKIzinSuresiGun = 0
        else :
            kayitEkle.PTKIzinSuresiGun = PersonelKullanilanizinGun
        
        if kayitEkle.PTKIzinSuresiSaat == None:
            kayitEkle.PTKIzinSuresiSaat = 0
        else :
            kayitEkle.PTKIzinSuresiSaat = PersonelKullanilanizinSaat
                
    else :
        kayitEkle.PTKHakedilenIzinYil = HesaplamaIzinYil(kayitEkle.PTKIseGiristarihi)
        kayitEkle.PTKHakedilenIzinGun = HesaplamaIzinGun(kayitEkle.PTKIseGiristarihi)
        if kayitEkle.PTKHakedilenIzinGun == None:
            kayitEkle.PTKkalanizin = -PersonelKullanilanizinGun
        elif PersonelKullanilanizinGun == None:
            kayitEkle.PTKkalanizin = kayitEkle.PTKHakedilenIzinGun
        elif PersonelKullanilanizinGun == None or kayitEkle.PTKHakedilenIzinGun == None:
            kayitEkle.PTKkalanizin = 0
        else :
            kayitEkle.PTKkalanizin = kayitEkle.PTKHakedilenIzinGun - PersonelKullanilanizinGun
            
        if kayitEkle.PTKIzinSuresiGun == None:
            kayitEkle.PTKIzinSuresiGun = 0
        else :
            kayitEkle.PTKIzinSuresiGun = PersonelKullanilanizinGun
            
        if kayitEkle.PTKIzinSuresiSaat == None:
            kayitEkle.PTKIzinSuresiSaat = 0
        else :
            kayitEkle.PTKIzinSuresiSaat = PersonelKullanilanizinSaat
            
    kayitEkle.save()
    PTKDefteriKayit_listesi = PerTakipKayit.objects.filter(PTKAktif__in=[True], PTKDurumu__in=["Çalışıyor"])
    paginator = Paginator(PTKDefteriKayit_listesi, 20 ) # Show 25 contacts per page
    Sayfa = request.GET.get('Sayfa')
    PersonelKayits = paginator.get_page(Sayfa)
    messages.success(request, "Kayıt Başarıyla Güncellendi...")
    messages.info(request, "Personel Hakedilen İzinler Hesaplama Yapıldı...")
    return render(request, "PTK/PTKkayitacikizindurum.html", {'PersonelKayits': PersonelKayits})


# ------------------ PTK Izin işlemleri ---------------

@permission_required('PerTakip.view_perizindurum')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKIzinKayit(request):
    logging.basicConfig(filename='Log/PTKkayitdebug.log', level=logging.DEBUG)
    Kelime = request.GET.get("Kelime")
    print(Kelime)
        
    if Kelime:
        PTKDefteriKayit_listesi = PerTakipKayit.objects.filter(Q(PTKAktif__in=[True]) & Q(PTKTckimlik__contains=Kelime) | Q(PTKAdiSoyadi__icontains=Kelime) | Q(PTKAdres__icontains=Kelime) | Q(PTKIl__icontains=Kelime) |Q(PTKAciklama__icontains=Kelime) & Q(PTKDurumu__in="Çalışıyor"))
        print(" kelime var arama çalışanlarda yapılıyor.", Kelime, PTKDefteriKayit_listesi)
    else:
        PTKDefteriKayit_listesi = PerTakipKayit.objects.filter(PTKAktif__in=[True], PTKDurumu__in=["Çalışıyor"])
    
    if Kelime:
        PTKIzinKayit_listesi = PerIzinDurum.objects.filter(Q(PerIzinAktif__in=[True]) & Q(PerIzinKonu__icontains=Kelime)| Q(PerIzinDonemi__icontains=Kelime) | Q(PerAdiSoyadi__icontains=Kelime))
        print(" kelime var arama çalışanlarda yapılıyor.", Kelime, PTKIzinKayit_listesi)
    else:
        PTKIzinKayit_listesi = PerIzinDurum.objects.filter(PerIzinAktif__in=[True])
    paginator = Paginator(PTKIzinKayit_listesi, 20 ) # Show 25 contacts per page

    Sayfa = request.GET.get('Sayfa')
    PersonelKayits = paginator.get_page(Sayfa)
    print()
    return render(request, "PTK/PTKIzinKayit.html", {'PersonelKayits': PersonelKayits, 'PTKDefteriKayit_listesi':PTKDefteriKayit_listesi})


@permission_required('PerTakip.add_perizindurum')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKIzinEkle(request):
    logging.basicConfig(filename='Log/IzinEkledebug.log', level=logging.DEBUG)
    form = PerIzinDurumKayitForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        kayitEkle = form.save(commit=False)
        kayitEkle.PerAdiSoyadi = kayitEkle.PerTakipKayit.PTKAdiSoyadi
        kayitEkle.PerIzinUser = request.user
        kayitEkle.save()
        messages.success(request, "Kayıt Girişi Yapıldı.")
        return redirect("/PerTakip/PTKIzinEkle/")
    return render(request, "PTK/PTKIzinEkleme.html", {"form": form})

@permission_required('PerTakip.change_perizindurum')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKIzinGuncelle(request, id):
    logging.basicConfig(filename='Log/PTKkayitGuncelledebug.log', level=logging.DEBUG)
    Kayits = get_object_or_404(PerIzinDurum, id=id)
    #if request.user != Kayits.PerIzinUser and request.user.is_superuser != True:
    #    return HttpResponseForbidden(" Yetkiniz Yoktur.!!!")
    request.session['kayitGuncelleID'] = id
    form = PerIzinDurumForm(request.POST or None, request.FILES or None, instance=Kayits)
    if form.is_valid():
        kayitEkle = form.save(commit=False)
        kayitEkle.save()
        messages.success(request, "Kayıt Başarıyla Güncellendi...")
    return render(request, "PTK/PTKIzinGuncelleme.html", {"form": form})


@permission_required('PerTakip.delete_perizindurum')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKIzinSil(request, id):
    logging.basicConfig(filename='Log/PTKkayitSildebug.log', level=logging.DEBUG)
    kayits = get_object_or_404(PerIzinDurum, id=id)
    #if request.user != kayits.PTKKayitUser and request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    request.session['kayitGuncelleID'] = id
    kayits.PerIzinAktif = False
    kayits.save()
    messages.info(request, "Kayıt Başarıyla Silindi...")
    return redirect("PerTakip:PTKIzinKayit")

@permission_required('PerTakip.view_perizindurum')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKIzinDetay(request, id):
    logging.basicConfig(filename='Log/PTKkayitdebug.log', level=logging.DEBUG)
    PersonelKayit = get_object_or_404(PerIzinDurum, id=id)
    PersonelKayitNot = PerIzinDurum.objects.filter(PerTakipKayit=id)
    request.session['kayitDetayID'] = id
    return render(request, "PTK/PTKIzinDetay.html", {"PersonelKayit": PersonelKayit,
                                                      "PersonelKayitNot": PersonelKayitNot})


#----------------- Duyurular ---------------

@permission_required('PerTakip.add_ptkduyurular')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKduyuruEkle(request):
    logging.basicConfig(filename='Log/PTKduyurudebug.log', level=logging.DEBUG)
    form = PTKDuyurularEkleForm(data=request.POST or None, files=request.FILES or None)
    if form.is_valid():
        DuyuruEkle = form.save(commit=False)
        DuyuruEkle.DuyuruUser = request.user
        DuyuruEkle.save()
        messages.success(request, "Duyuru Başarıyla Yayınlandı.")
        return redirect("/PerTakip/PTKDuyuruEkle/")
    return render(request, "PTK/PTKDuyuruEkle.html", {"form": form})

@permission_required('PerTakip.view_ptkduyurular')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKduyurular(request):
    logging.basicConfig(filename='Log/PTKduyurudebug.log', level=logging.DEBUG)
    Duyurular_listesi = PTKDuyurular.objects.filter(PTKDuyuruAktif__in=[True])

    paginator = Paginator(Duyurular_listesi, 20 ) # Show 25 contacts per page

    Sayfa = request.GET.get('Sayfa')
    Duyurulars = paginator.get_page(Sayfa)

    return render(request, "PTK/PTKDuyurular.html", {"Duyurulars": Duyurulars})

@permission_required('PerTakip.view_ptkduyurular')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKDuyuruDetay(request, id):
    logging.basicConfig(filename='Log/PTKduyurudebug.log', level=logging.DEBUG)
    duyurular = get_object_or_404(PTKDuyurular, id=id)
    return render(request, "PTK/PTKDuyuruDetay.html", {"duyurular": duyurular})

@permission_required('PerTakip.change_ptkduyurular')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKduyuruGuncelle(request, id):
    logging.basicConfig(filename='Log/PTKduyurudebug.log', level=logging.DEBUG)
    Kayits = get_object_or_404(PTKDuyurular, id=id)
    #if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    form = PTKDuyurularEkleForm(request.POST or None, files=request.FILES or None, instance=Kayits)
    if form.is_valid():
        kayitEkle = form.save(commit=False)
        kayitEkle.save()

        messages.success(request, "Kayıt Başarıyla Güncellendi...")
    return render(request, "PTK/PTKDuyuruGuncelle.html", {"form": form})


# ------------------- user profiller --------------

@login_required(login_url="user:login")
def PTKUserprofil(request):
    if request.method == 'POST':
        form = UserEkleForm(data=request.POST, instance=request.user)
        update = form.save(commit=False)
        update.user = request.user
        update.save()
        messages.success(request, "Başarıyla Günceleme Yaptınız...")
    else:
        form = UserEkleForm(instance=request.user)
        messages.info(request, "Günceleme Yapılmadı...")
    return render(request, "PTK/Userprofil.html", {"form" : form})


def PTKUserPasswordChange(request):
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
    return render(request, 'PTK/UserPasswordChange.html', {'form': form})

#----------------- PerTakip PTK Ekleme --------------------

@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKkayitNotGuncelle(request, id):
    pass

@permission_required('PerTakip.add_PerTakipNotlar')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKkayitNotEkle(request,id):
    logging.basicConfig(filename='Log/PTKDefteriNotEkledebug.log', level=logging.DEBUG)
    request.session['kayitGuncelleID'] = id
    form = PerTakipNotlarForm(data=request.POST or None, files=request.FILES or None)
    kayits = get_object_or_404(PerTakipKayit, id=id)
    if form.is_valid():
        NewPTKEkle = form.save(commit=False)
        NewPTKEkle.PerTakipNotUser = request.user
        NewPTKEkle.PerTakipKayit = kayits
        NewPTKEkle.save()
        messages.success(request, "Personele Not Başarıyla Kayıt Edildi..")
    return render(request, "PTK/PTKkayitNotEkle.html", {"form": form})

@permission_required('PerTakip.view_PerTakipNotlar')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKkayitNotDetay(request, id):
    logging.basicConfig(filename='Log/PTKDefteriNotEkledebug.log', level=logging.DEBUG)
    DestekTalebiKayit1 = get_object_or_404(PerTakipKayit, id=id)
    DestekTalebiNotlars = PerTakipNotlar.objects.filter(PerTakipNotAktif__in=[True])
    request.session['kayitGuncelleID'] = id
    return render(request, "PTK/PTKkayitDetay.html", {"DestekTalebiNotlars": DestekTalebiNotlars,
                                                      "DestekTalebiKayit": DestekTalebiKayit1})


@permission_required('PerTakip.delete_PTKdefteriPTKlar')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def PTKkayitNotSil(request, id):
    logging.basicConfig(filename='Log/DestekTalebiPTKEkledebug.log', level=logging.DEBUG)
    kayits = get_object_or_404(PerTakipNotlar, id=id)
    kayits.PerTakipNotAktif=False
    kayits.save()
    messages.info(request, "Kayıt Başarıyla Silindi...")
    return redirect("PerTakip:PTKkayitDetay")



#-----------------   xls döküm alınması ----------------

@xframe_options_sameorigin
@login_required(login_url="user:login")
def export_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="PerListesi.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Çalışan Personel Sayısı')
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ["id", "PTKTckimlik", "PTKAdiSoyadi","PTKFirmaAdi","PTKAdres","PTKIlce","PTKEmail","PTKTelefon", "PTKGorevi","PTKAciklama", "PTKIseGiristarihi", "PTKIseCikistarihi","PTKHakedilenIzinYil","PTKHakedilenIzinGun","PTKDurumu"]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows = PerTakipKayit.objects.filter(Q(PTKAktif__in=[True]) & Q(PTKDurumu="Çalışıyor")).select_related('PTKTckimlik').values_list( "id", "PTKTckimlik", "PTKAdiSoyadi", "PTKFirmaAdi","PTKAdres","PTKIlce","PTKEmail","PTKTelefon", "PTKGorevi","PTKAciklama","PTKIseGiristarihi", "PTKIseCikistarihi","PTKHakedilenIzinYil","PTKHakedilenIzinGun","PTKDurumu")
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response

@xframe_options_sameorigin
@login_required(login_url="user:login")
def export_ayrilanxls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="PerListesi.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Çalışan Personel Sayısı')
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ["id", "PTKTckimlik", "PTKAdiSoyadi","PTKFirmaAdi","PTKAdres","PTKIlce","PTKEmail","PTKTelefon", "PTKGorevi","PTKAciklama", "PTKIseGiristarihi", "PTKIseCikistarihi","PTKHakedilenIzinYil","PTKHakedilenIzinGun","PTKDurumu"]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows = PerTakipKayit.objects.filter(Q(PTKAktif__in=[True]) & Q(PTKDurumu="Ayrıldı")).select_related('PTKTckimlik').values_list( "id", "PTKTckimlik", "PTKAdiSoyadi", "PTKFirmaAdi","PTKAdres","PTKIlce","PTKEmail","PTKTelefon", "PTKGorevi","PTKAciklama","PTKIseGiristarihi", "PTKIseCikistarihi","PTKHakedilenIzinYil","PTKHakedilenIzinGun","PTKDurumu")
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response