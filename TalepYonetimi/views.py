from django.shortcuts import render, redirect, get_object_or_404
from .forms import DestekTalebiTuruEkleForm, KategoriEkleForm, UygulamaEkleForm, DuyuruEklefullForm, DuyuruGuncelleForm
from .forms import KurumlarEkleForm, KurumBirimiEkleForm, KisiEkleForm, DestekTalebiForm, DuyuruEkleForm, \
    DestekTalebiNotlarForm, UserEkleForm
from django.contrib import messages
from TalepYonetimi.models import DestekTalebiTuru, Kategori, Uygulama, Kurumlar, KurumBirimi, Kisi, Duyurular
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Count, Q
from .models import DestekTalebiKayit, DestekTalebiNotlar
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator
from django.contrib.auth.forms import PasswordChangeForm

from django.utils.text import slugify
# from django.views.decorators.cache import cache_page
from django.views.decorators.clickjacking import xframe_options_deny, xframe_options_exempt, xframe_options_sameorigin
from django.contrib.auth.decorators import permission_required

import csv
import xlwt
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy.random import randn
from pylab import *
from matplotlib import pylab
import logging
import matplotlib
import io
from Lib import base64
import urllib
from numpy.core import arange
from math import cos, sin
from datetime import date, timedelta
from Lib.base64 import decode, encode


# Create your views here.
# -------------------kurumbirim ---------------


# @xframe_options_deny    ---- Herhangi bir karede görüntülenmeyeceğim
# @xframe_options_exempt    --- Bu sayfa herhangi bir sitede bir çerçeveye yüklemek için güvenlidir
# --- Benimkiyle aynı kaynaktan gelen bir çerçevede görüntüle.

@permission_required('TalepYonetimi.view_kurumbirimi')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def kurumBirimi(request):
    logging.basicConfig(filename='Log/KurumBirimdebug.log', level=logging.DEBUG)
    KurumBirimis = KurumBirimi.objects.filter(BirimAktif=True)
    context = {
        "KurumBirimis": KurumBirimis
    }
    return render(request, "TLP/TLPkurumBirimi.html", context)


@permission_required('TalepYonetimi.add_kurumbirimi')
@xframe_options_sameorigin
@login_required(login_url="user:login")
# @cache_page(60 * 15)
def kurumBirimiEkle(request):
    logging.basicConfig(filename='Log/kayitlar.log', level=logging.DEBUG)
    # if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    form = KurumBirimiEkleForm(request.POST or None)
    if form.is_valid():
        kurumBirimiEkle = form.save(commit=False)
        kurumBirimiEkle.BirimKurumAdi = kurumBirimiEkle.KurumAdi
        kurumBirimiEkle.save()
        messages.success(request, "Kayıt Girişi Yapıldı.")
        return redirect("/TalepYonetimi/TLPkurumBirimiEkle/")
    return render(request, "TLP/TLPkurumBirimiEkle.html", {"form": form})


@permission_required('TalepYonetimi.view_kurumbirimi')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def KurumBirimiDetay(request, id):
    logging.basicConfig(filename='Log/KurumBirimdebug.log', level=logging.DEBUG)
    # if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    kurumBirimi = get_object_or_404(KurumBirimi, id=id)
    return render(request, "TLP/TLPkurumBirimiDetay.html", {"kurumBirimi": kurumBirimi})


@permission_required('TalepYonetimi.view_kurumbirimi')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def kurumBirimiGuncelle(request, id):
    logging.basicConfig(filename='Log/KurumBirimdebug.log', level=logging.DEBUG)
    # if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    kurumBirimi = get_object_or_404(KurumBirimi, id=id)
    form = KurumBirimiEkleForm(request.POST or None, request.FILES or None, instance=kurumBirimi)

    request.session['kurumBirimiGuncelleID'] = id

    if form.is_valid():
        kurumBirimiEkle = form.save(commit=False)
        if kurumBirimiEkle.KurumAdi:
            kurumBirimiEkle.BirimKurumAdi = str(kurumBirimiEkle.KurumAdi)
        kurumBirimiEkle.save()

        messages.success(request, "Kayıt Başarıyla Güncellendi...")
        return redirect("TalepYonetimi:kurumBirimi")

    return render(request, "TLP/TLPkurumBirimiGuncelle.html", {"form": form})


@permission_required('TalepYonetimi.delete_kurumbirimi')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def kurumBirimiSil(request, id):
    logging.basicConfig(filename='Log/KurumBirimdebug.log', level=logging.DEBUG)
    # if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    kurumBirimi = get_object_or_404(KurumBirimi, id=id)
    kurumBirimi.BirimAktif = False
    kurumBirimi.save()
    messages.info(request, "Kayıt Başarıyla Silindi...")
    return redirect("TalepYonetimi:kurumBirimi")


# --------------------- kurumlar ---------------------

@xframe_options_sameorigin
@login_required(login_url="user:login")
def kurumlar(request):
    logging.basicConfig(filename='Log/Kurumlardebug.log', level=logging.DEBUG)
    # if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    Kurumlars = Kurumlar.objects.filter(KurumAktif=True)
    context = {
        "Kurumlars": Kurumlars
    }
    return render(request, "TLP/TLPkurumlar.html", context)


@permission_required('TalepYonetimi.add_kurumlar')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def kurumlarEkle(request):
    logging.basicConfig(filename='Log/Kurumlardebug.log', level=logging.DEBUG)
    # if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    form = KurumlarEkleForm(request.POST or None)

    if form.is_valid():
        kurumlarEkle = form.save(commit=False)
        kurumlarEkle.save()

        messages.success(request, "Kayıt Girişi Yapıldı.")
        return redirect("/TalepYonetimi/TLPkurumlarEkle/")
    return render(request, "TLP/TLPkurumlarEkle.html", {"form": form})


@permission_required('TalepYonetimi.change_kurumlar')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def kurumlarGuncelle(request, id):
    logging.basicConfig(filename='Log/Kurumlardebug.log', level=logging.DEBUG)
    # if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    kurumlar = get_object_or_404(Kurumlar, id=id)
    form = KurumlarEkleForm(request.POST or None, request.FILES or None, instance=kurumlar)
    request.session['kurumlarGuncelleID'] = id

    if form.is_valid():
        kurumlarEkle = form.save(commit=False)
        kurumlarEkle.save()

        messages.success(request, "Kayıt Başarıyla Güncellendi...")
        return redirect("TalepYonetimi:kurumlar")
    return render(request, "TLP/TLPkurumlarGuncelle.html", {"form": form})


@permission_required('TalepYonetimi.delete_kurumlar')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def kurumlarSil(request, id):
    logging.basicConfig(filename='Log/Kurumlardebug.log', level=logging.DEBUG)
    # if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    kurumlar = get_object_or_404(Kurumlar, id=id)
    kurumlar.KurumAktif = False
    kurumlar.save()
    messages.info(request, "Kayıt Başarıyla Silindi...")
    return redirect("TalepYonetimi:kurumlar")


@permission_required('TalepYonetimi.view_kurumlar')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def KurumlarDetay(request, id):
    kurumlar = get_object_or_404(Kurumlar, id=id)
    kbirimler = KurumBirimi.objects.filter(KurumAdi_id=id, KurumAdi__KurumAktif=True)
    DestekTalebiSayisi = len(DestekTalebiKayit.objects.filter(DestekTalebiKurum=id))

    return render(request, "TLP/TLPkurumlarDetay.html", {"kurumlar": kurumlar, "kbirimler": kbirimler,
                                                         "DestekTalebiSayisi": DestekTalebiSayisi})


# ------------------ uygulama tanımlama

@permission_required('TalepYonetimi.view_uygulama')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def uygulama(request):
    logging.basicConfig(filename='Log/uygulamadebug.log', level=logging.DEBUG)
    # if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    Uygulamas = Uygulama.objects.filter(UygulamaAktif=True)
    context = {
        "Uygulamas": Uygulamas
    }
    return render(request, "TLP/TLPuygulama.html", context)


@permission_required('TalepYonetimi.add_uygulama')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def uygulamaEkle(request):
    logging.basicConfig(filename='Log/uygulamadebug.log', level=logging.DEBUG)
    # if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    form = UygulamaEkleForm(request.POST or None)

    if form.is_valid():
        uygulamaEkle = form.save(commit=False)
        uygulamaEkle.save()

        messages.success(request, "Kayıt Girişi Yapıldı.")
        return redirect("/TalepYonetimi/TLPuygulamaEkle/")
    return render(request, "TLP/TLPuygulamaEkle.html", {"form": form})


@permission_required('TalepYonetimi.change_uygulama')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def uygulamaGuncelle(request, id):
    logging.basicConfig(filename='Log/uygulamadebug.log', level=logging.DEBUG)
    # if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    uygulama = get_object_or_404(Uygulama, id=id)
    form = UygulamaEkleForm(request.POST or None, request.FILES or None, instance=uygulama)
    request.session['uygulamaGuncelleID1'] = id
    if form.is_valid():
        uygulamaEkle = form.save(commit=False)
        uygulamaEkle.save()

        messages.success(request, "Kayıt Başarıyla Güncellendi...")
        return redirect("TalepYonetimi:uygulama")
    return render(request, "TLP/TLPuygulamaGuncelle.html", {"form": form})


@permission_required('TalepYonetimi.delete_uygulama')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def uygulamaSil(request, id):
    logging.basicConfig(filename='Log/uygulamadebug.log', level=logging.DEBUG)
    # if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    uygulama = get_object_or_404(Uygulama, id=id)
    uygulama.UygulamaAktif = False
    uygulama.save()
    messages.info(request, "Kayıt Başarıyla Silindi...")
    return redirect("TalepYonetimi:uygulama")


# -------------- index işlemleri -------------------


@xframe_options_sameorigin
@login_required(login_url="user:login")
def TLPindex(request):
    logging.basicConfig(filename='Log/TLPindexdebug.log', level=logging.DEBUG)
    Duyurulars = Duyurular.objects.filter(DuyuruAktif=True or None, DuyuruUygulama='2')| Duyurular.objects.filter(DuyuruAktif=True or None, DuyuruUygulama='0')

    DestekTalebiKayits = DestekTalebiKayit.objects.filter(DestekTalebiAktif=True)

    formAktif = DestekTalebiKayit.objects.filter(DestekTalebiDurumu="Açık")
    DestekTalebisayisiAktif = len(formAktif)
    request.session['DestekTalebisayisiAktifs'] = DestekTalebisayisiAktif

    formfalse = DestekTalebiKayit.objects.filter(DestekTalebiDurumu="Kapalı")
    DestekTalebisayisiPasif = len(formfalse)
    request.session['DestekTalebisayisiPasifs'] = DestekTalebisayisiPasif

    form = DestekTalebiKayit.objects.filter()
    DestekTalebisayisi = len(form)
    request.session['DestekTalebisayisis'] = DestekTalebisayisi

    formKisiSayi = Kisi.objects.filter(KisiAktif=True)
    KisiSayi = len(formKisiSayi)
    request.session["KisiSayisi"] = KisiSayi

    formUygulamaSayi = Uygulama.objects.filter(UygulamaAktif=True)
    UygulamaSayi = len(formUygulamaSayi)
    request.session["UygulamaSayisi"] = UygulamaSayi

    formKurumSayisi = Kurumlar.objects.filter(KurumAktif=True)
    KurumSayisi = len(formKurumSayisi)
    request.session["KurumSayisis"] = KurumSayisi

    formBirimSayisi1 = KurumBirimi.objects.filter(BirimAktif=True)
    BirimSayisi = len(formBirimSayisi1)
    request.session["BirimSayisis"] = BirimSayisi

    return render(request, "TLP/TLPindex.html", {'Duyurulars': Duyurulars, "DestekTalebiKayits": DestekTalebiKayits})


@permission_required('TalepYonetimi.view_destektalebituru')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def destekTalebiTuru(request):
    logging.basicConfig(filename='Log/DestekTalebiTurudebug.log', level=logging.DEBUG)
    # if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    DestekTalebiTurus = DestekTalebiTuru.objects.filter(DestekTalebiAktif=True)
    context = {
        "DestekTalebiTurus": DestekTalebiTurus
    }
    return render(request, "TLP/TLPDestekTalebiTuru.html", context)


@permission_required('TalepYonetimi.add_destektalebituru')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def DestekTalebiTuruEkle(request):
    logging.basicConfig(filename='Log/DestekTalebiTurudebug.log', level=logging.DEBUG)
    # if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    form = DestekTalebiTuruEkleForm(request.POST or None)

    if form.is_valid():
        DestekTalebiTuruEkle = form.save(commit=False)
        DestekTalebiTuruEkle.save()

        messages.success(request, "Kayıt Girişi Yapıldı.")
        return redirect("/TalepYonetimi/TLPDestekTalebiTuruEkle/")
    return render(request, "TLP/TLPDestekTalebiTuruEkle.html", {"form": form})


@permission_required('TalepYonetimi.change_destektalebituru')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def DestekTalebiTuruGuncelle(request, id):
    logging.basicConfig(filename='Log/DestekTalebiTurudebug.log', level=logging.DEBUG)
    # if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    destekTalebiTuru = get_object_or_404(DestekTalebiTuru, id=id)
    form = DestekTalebiTuruEkleForm(request.POST or None,
                                    request.FILES or None, instance=destekTalebiTuru)
    request.session['DestekTalebiTuruGuncelleID1'] = id
    if form.is_valid():
        DestekTalebiTuruEkle = form.save(commit=False)
        DestekTalebiTuruEkle.save()

        messages.success(request, "Kayıt Başarıyla Güncellendi...")
        return redirect("TalepYonetimi:DestekTalebiTuru")
    return render(request, "TLP/TLPDestekTalebiTuruGuncelle.html", {"form": form})


@permission_required('TalepYonetimi.delete_destektalebituru')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def DestekTalebiTuruSil(request, id):
    logging.basicConfig(filename='Log/DestekTalebiTurudebug.log', level=logging.DEBUG)
    # if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    destekTalebiTuru = get_object_or_404(DestekTalebiTuru, id=id)
    destekTalebiTuru.DestekTalebiAktif = False
    destekTalebiTuru.save()
    messages.info(request, "Kayıt Başarıyla Silindi...")
    return redirect("TalepYonetimi:DestekTalebiTuru")


@permission_required('TalepYonetimi.view_kategori')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def kategori(request):
    logging.basicConfig(filename='Log/kategoridebug.log', level=logging.DEBUG)
    Kategoris = Kategori.objects.filter(KategoriAktif=True)
    context = {
        "Kategoris": Kategoris
    }
    return render(request, "TLP/TLPkategori.html", context)


@permission_required('TalepYonetimi.add_kategori')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def kategoriEkle(request):
    logging.basicConfig(filename='Log/kategoridebug.log', level=logging.DEBUG)
    # if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    form = KategoriEkleForm(request.POST or None)

    if form.is_valid():
        kategoriEkle = form.save(commit=False)
        kategoriEkle.save()
        messages.success(request, "Kayıt Girişi Yapıldı.")
        return redirect("/TalepYonetimi/TLPkategoriEkle/")
    return render(request, "TLP/TLPkategoriEkle.html", {"form": form})


@permission_required('TalepYonetimi.change_kategori')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def kategoriGuncelle(request, id):
    logging.basicConfig(filename='Log/kategoridebug.log', level=logging.DEBUG)
    # if request.user.is_superuser != True:
    #    return HttpResponseForbidden()

    kategori = get_object_or_404(Kategori, id=id)
    form = KategoriEkleForm(request.POST or None,
                            request.FILES or None, instance=kategori)
    request.session['kategoriGuncelleID'] = id
    if form.is_valid():
        kategoriEkle = form.save(commit=False)
        kategoriEkle.save()

        messages.success(request, "Kayıt Başarıyla Güncellendi...")
        return redirect("TalepYonetimi:kategori")
    return render(request, "TLP/TLPkategoriGuncelle.html", {"form": form})


@permission_required('TalepYonetimi.delete_kategori')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def kategoriSil(request, id):
    logging.basicConfig(filename='Log/kategoridebug.log', level=logging.DEBUG)
    # if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    kategori = get_object_or_404(Kategori, id=id)
    kategori.KategoriAktif = False
    kategori.save()
    messages.info(request, "Kayıt Başarıyla Silindi...")
    return redirect("TalepYonetimi:kategori")


@permission_required('TalepYonetimi.view_kisi')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def kisi(request):
    logging.basicConfig(filename='Log/kisidebug.log', level=logging.DEBUG)
    kisis = Kisi.objects.filter(KisiAktif=True)
    context = {
        "kisis": kisis
    }
    return render(request, "TLP/TLPkisi.html", context)


@permission_required('TalepYonetimi.add_kisi')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def kisiEkle(request, renderer=None):
    logging.basicConfig(filename='Log/kisidebug.log', level=logging.DEBUG)
    form = KisiEkleForm(request.POST or None, files=request.FILES or None)

    if form.is_valid():
        kisiEkle = form.save(commit=False)
        kisiEkle.KisiUser = request.user
        kisiEkle.save()

        messages.success(request, "Kayıt Girişi Yapıldı.")
        return redirect("/TalepYonetimi/TLPkisiEkle/")
    return render(request, "TLP/TLPkisiEkle.html", {"form": form})


@permission_required('TalepYonetimi.view_kisi')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def kisiDetay(request, id):
    logging.basicConfig(filename='Log/kisidebug.log', level=logging.DEBUG)
    kisiDetay = get_object_or_404(Kisi, id=id)
    return render(request, "TLP/TLPkisiDetay.html", {"kisiDetay": kisiDetay})


@permission_required('TalepYonetimi.change_kisi')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def kisiGuncelle(request, id):
    logging.basicConfig(filename='Log/kisidebug.log', level=logging.DEBUG)
    # if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    kisi = get_object_or_404(Kisi, id=id)
    form = KisiEkleForm(request.POST or None, files=request.FILES or None, instance=kisi)
    request.session['kisiGuncelleID1'] = id
    if form.is_valid():
        kisiEkle = form.save(commit=False)
        kisiEkle.save()

        messages.success(request, "Kayıt Başarıyla Güncellendi...")
        return redirect("TLP/TLPkisi.html")
    return render(request, "TLP/TLPkisiGuncelle.html", {"form": form})


@permission_required('TalepYonetimi.delete_kisi')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def kisiSil(request, id):
    logging.basicConfig(filename='Log/kisidebug.log', level=logging.DEBUG)
    # if request.user.is_superuser != True:
    #    return HttpResponseForbidden()
    kisi = get_object_or_404(Kisi, id=id)
    kisi.KisiAktif = False
    kisi.save()
    messages.info(request, "Kayıt Başarıyla Silindi...")
    return redirect("TalepYonetimi:kisi")


# ------------------ kayıt işlemleri ---------------

@permission_required('TalepYonetimi.view_destektalebikayit')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def kayitacik(request):
    logging.basicConfig(filename='Log/kayitdebug.log', level=logging.DEBUG)
    Kelime = request.GET.get("Kelime")
    print(Kelime)
    if Kelime:
        DestekTalebiKayitlar_listesi = DestekTalebiKayit.objects.filter(Q(DestekTalebiAktif=True,DestekTalebiDurumu="Açık",) & (Q(DestekTalebiKonu__icontains=Kelime)|Q(DestekTalebiAciklama__icontains=Kelime)|Q(DestekTalebiKisi__icontains=Kelime)))
        #DestekTalebiKayitlar_listesi = DestekTalebiKayit.objects.filter(DestekTalebiAktif=True,
        #                                                                DestekTalebiKonu__contains=Kelime,
        #                                                                DestekTalebiDurumu="Açık", )
    else:
        DestekTalebiKayitlar_listesi = DestekTalebiKayit.objects.filter(DestekTalebiAktif=True,
                                                                        DestekTalebiDurumu="Açık")
    paginator = Paginator(DestekTalebiKayitlar_listesi, 20)  # Show 25 contacts per page

    Sayfa = request.GET.get('Sayfa')
    DestekTalebiKayits = paginator.get_page(Sayfa)
    return render(request, "TLP/TLPkayitacik.html", {'DestekTalebiKayits': DestekTalebiKayits})


@permission_required('TalepYonetimi.view_destektalebikayit')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def kayitkapali(request):
    logging.basicConfig(filename='Log/kayitdebug.log', level=logging.DEBUG)
    Kelime = request.GET.get("Kelime")
    if Kelime:
        DestekTalebiKayitlar_listesi = DestekTalebiKayit.objects.filter(Q(DestekTalebiAktif=True,DestekTalebiDurumu="Kapalı",) & (Q(DestekTalebiKonu__icontains=Kelime)|Q(DestekTalebiAciklama__icontains=Kelime)|Q(DestekTalebiKisi__icontains=Kelime)))
        #DestekTalebiKayitlar_listesi = DestekTalebiKayit.objects.filter(DestekTalebiAktif=True,
        #                                                                DestekTalebiKonu__contains=Kelime,
        #                                                                DestekTalebiDurumu="Kapalı", )
    else:
        DestekTalebiKayitlar_listesi = DestekTalebiKayit.objects.filter(DestekTalebiAktif=True,
                                                                        DestekTalebiDurumu="Kapalı")
    paginator = Paginator(DestekTalebiKayitlar_listesi, 20)  # Show 25 contacts per page

    Sayfa = request.GET.get('Sayfa')
    DestekTalebiKayits = paginator.get_page(Sayfa)
    return render(request, "TLP/TLPkayitkapali.html", {'DestekTalebiKayits': DestekTalebiKayits})

@xframe_options_exempt
@permission_required('TalepYonetimi.add_destektalebikayit')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def kayitEkle(request):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    # labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    # sizes = [15, 30, 45, 10]
    # explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    # fig1, ax1 = plt.subplots()
    # ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
    #        shadow=True, startangle=90)
    # ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # plt.show()
    # matplotlib.axes.Axes.pie
    # matplotlib.pyplot.pie

    logging.basicConfig(filename='Log/kayitdebug.log', level=logging.DEBUG)
    form = DestekTalebiForm(request.POST or None, request.FILES or None, )
    if form.is_valid():
        kayitEkle = form.save(commit=False)
        kayitEkle.DestekTalebiUser = request.user
        kayitEkle.save()
        messages.success(request, "Kayıt Girişi Yapıldı.")
        return redirect("/TalepYonetimi/TLPkayitEkle/")
    return render(request, "TLP/TLPkayitEkleme.html", {"form": form})


@permission_required('TalepYonetimi.change_destektalebikayit')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def kayitGuncelle(request, id):
    logging.basicConfig(filename='Log/kayitdebug.log', level=logging.DEBUG)
    Kayits = get_object_or_404(DestekTalebiKayit, id=id)
    # if request.user != Kayits.DestekTalebiUser or request.user.is_superuser != True:
    # return HttpResponseForbidden()
    request.session['kayitGuncelleID'] = id
    form = DestekTalebiForm(request.POST or None, request.FILES or None, instance=Kayits)
    if form.is_valid():
        kayitEkle = form.save(commit=False)
        kayitEkle.save()
        messages.success(request, "Kayıt Başarıyla Güncellendi...")
    return render(request, "TLP/TLPkayitGuncelleme.html", {"form": form})


@permission_required('TalepYonetimi.delete_destektalebikayit')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def kayitSil(request, id):
    logging.basicConfig(filename='Log/kayitdebug.log', level=logging.DEBUG)
    kayits = get_object_or_404(DestekTalebiKayit, id=id)
    if request.user != kayits.DestekTalebiUser and request.user.is_superuser != True:
        return HttpResponseForbidden()
    kayits.DestekTalebiAktif = False
    kayits.save()
    messages.info(request, "Kayıt Başarıyla Silindi...")
    return redirect("TalepYonetimi:kayitacik")


@permission_required('TalepYonetimi.view_destektalebikayit')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def kayitDetay(request, id):
    logging.basicConfig(filename='Log/kayitdebug.log', level=logging.DEBUG)
    destekTalebiKayit = get_object_or_404(DestekTalebiKayit, id=id)
    DestekTalebiNot = DestekTalebiNotlar.objects.filter(DestekTalebiKayit=id)
    request.session['kayitDetayID'] = id
    return render(request, "TLP/TLPkayitDetay.html", {"DestekTalebiKayit": destekTalebiKayit,
                                                      "DestekTalebiNot": DestekTalebiNot})


@xframe_options_sameorigin
@login_required(login_url="user:login")
def DestekTalebiNotGuncelle(request, id):
    pass


@permission_required('TalepYonetimi.add_destektalebinotlar')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def DestekTalebiNotEkle(request, id):
    logging.basicConfig(filename='Log/DestekTalebiNotEkledebug.log', level=logging.DEBUG)
    request.session['kayitGuncelleID'] = id
    form = DestekTalebiNotlarForm(data=request.POST or None, files=request.FILES or None)
    kayits = get_object_or_404(DestekTalebiKayit, id=id)
    if form.is_valid():
        NewNotEkle = form.save(commit=False)
        NewNotEkle.DestekTalebiNotUser = request.user
        NewNotEkle.DestekTalebiKayit = kayits
        NewNotEkle.save()
        messages.success(request, "Not Başarıyla Kayıt Edildi..")
    return render(request, "TLP/TLPDestekTalebiNotEkle.html", {"form": form})


@permission_required('TalepYonetimi.view_destektalebinotlar')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def DestekTalebiNotDetay(request, id):
    logging.basicConfig(filename='Log/DestekTalebiNotEkledebug.log', level=logging.DEBUG)
    DestekTalebiKayit1 = get_object_or_404(DestekTalebiKayit, id=id)
    DestekTalebiNotlars = DestekTalebiNotlar.objects.filter(DestekTalebiNotAktif=True)
    request.session['kayitGuncelleID'] = id
    return render(request, "TLP/TLPkayitDetay.html", {"DestekTalebiNotlars": DestekTalebiNotlars,
                                                      "DestekTalebiKayit1": DestekTalebiKayit1})


@permission_required('TalepYonetimi.delete_destektalebinotlar')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def DestekTalebiNotSil(request, id):
    logging.basicConfig(filename='Log/DestekTalebiNotEkledebug.log', level=logging.DEBUG)
    kayits = get_object_or_404(DestekTalebiNotlar, id=id)
    kayits.DestekTalebiNotAktif = False
    kayits.save()
    messages.info(request, "Kayıt Başarıyla Silindi...")
    return redirect("TalepYonetimi:kayitDetay")


@permission_required('TalepYonetimi.add_duyurular')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def duyuruEkle(request):
    logging.basicConfig(filename='Log/duyurudebug.log', level=logging.DEBUG)
    if request.user.is_superuser == True:
        form = DuyuruEklefullForm(data=request.POST or None, files=request.FILES or None)
    else:
        form = DuyuruEkleForm(data=request.POST or None, files=request.FILES or None)
    if form.is_valid():
        DuyuruEkle = form.save(commit=False)
        DuyuruEkle.DuyuruUser = request.user
        if request.user.is_superuser != True:
            DuyuruEkle.DuyuruUygulama = '2'
        DuyuruEkle.save()
        messages.success(request, "Duyuru Başarıyla Yayınlandı.")
        return redirect("/TalepYonetimi/TLPDuyuruEkle/")
    return render(request, "TLP/TLPDuyuruEkle.html", {"form": form})


@permission_required('TalepYonetimi.view_duyurular')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def duyurular(request):
    logging.basicConfig(filename='Log/duyurudebug.log', level=logging.DEBUG)
    Duyurular_listesi = Duyurular.objects.filter(Q(DuyuruUygulama='2')|Q(DuyuruUygulama='0'))
    paginator = Paginator(Duyurular_listesi, 20)  # Show 25 contacts per page
    Sayfa = request.GET.get('Sayfa')
    Duyurulars = paginator.get_page(Sayfa)

    return render(request, "TLP/TLPDuyurular.html", {"Duyurulars": Duyurulars})


@permission_required('TalepYonetimi.view_duyurular')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def DuyuruDetay(request, id):
    logging.basicConfig(filename='Log/duyurudebug.log', level=logging.DEBUG)
    duyurular = get_object_or_404(Duyurular, id=id)
    return render(request, "TLP/TLPDuyuruDetay.html", {"duyurular": duyurular})


@permission_required('TalepYonetimi.change_duyurular')
@xframe_options_sameorigin
@login_required(login_url="user:login")
def duyuruGuncelle(request, id):
    logging.basicConfig(filename='Log/duyurudebug.log', level=logging.DEBUG)
    Kayits = get_object_or_404(Duyurular, id=id)
    if request.user.is_superuser != True:
       return HttpResponseForbidden()
    if request.user.is_superuser == True:
        form = DuyuruGuncelleForm(request.POST or None, files=request.FILES or None, instance=Kayits)
    else:
        form = DuyuruGuncelleForm(request.POST or None, files=request.FILES or None, instance=Kayits)
    if form.is_valid():
        kayitEkle = form.save(commit=False)
        kayitEkle.save()

        messages.success(request, "Kayıt Başarıyla Güncellendi...")
    return render(request, "TLP/TLPDuyuruGuncelle.html", {"form": form})


@xframe_options_sameorigin
@login_required(login_url="user:login")
def DestekTalebiIstatistik(request):
 
    i =0
    x =[]
    y =[]
      

    startdate = date.today()
    baslangic= startdate + timedelta(days=1)
    enddate = startdate - timedelta(days=1)
    Haftalikenddate = startdate - timedelta(days=7)
    Aylikenddate = startdate - timedelta(days=30)


    DestekTalebiKisiler = DestekTalebiKayit.objects.filter(DestekTalebiAktif=True).values('DestekTalebiKisi').annotate(
        total=Count("DestekTalebiKisi")).order_by('DestekTalebiKisi')[:10][::1]
    DestekTalebiKayitlar = DestekTalebiKayit.objects.filter(DestekTalebiAktif=True).values('DestekTalebiKurum',
                                                                                           'DestekTalebiBirim').annotate(
        total=Count("DestekTalebiKurum")).order_by('DestekTalebiKurum')[:10][::1]

#----------------

    DestekTalebiKayitlartoplam = DestekTalebiKayit.objects.filter(DestekTalebiAktif=True).values(
        'DestekTalebiKurum').annotate(total=Count("DestekTalebiKurum")).order_by('DestekTalebiKurum')[::1]
    formtoplamsayi = DestekTalebiKayit.objects.filter(DestekTalebiAktif=True)
    DestekTalebiKayitlartoplamsayi = len(formtoplamsayi)

    DestekTalebiKayitlarAylik = DestekTalebiKayit.objects.filter(DestekTalebiBaslamaTarihi__range=[Aylikenddate, baslangic],DestekTalebiAktif=True).values(
        'DestekTalebiKurum').annotate(total=Count("DestekTalebiKurum")).order_by('DestekTalebiKurum')[::1]
    formAyliksayi = DestekTalebiKayit.objects.filter(DestekTalebiBaslamaTarihi__range=[Aylikenddate, baslangic],DestekTalebiAktif=True)
    DestekTalebiKayitlarAyliksayi = len(formAyliksayi)

    DestekTalebiKayitlarHaftalik = DestekTalebiKayit.objects.filter(DestekTalebiBaslamaTarihi__range=[Haftalikenddate, baslangic],DestekTalebiAktif=True).values(
        'DestekTalebiKurum').annotate(total=Count("DestekTalebiKurum")).order_by('DestekTalebiKurum')[::1]
    formHaftaliksayi = DestekTalebiKayit.objects.filter(DestekTalebiBaslamaTarihi__range=[Haftalikenddate, baslangic],DestekTalebiAktif=True)
    DestekTalebiKayitlarHaftaliksayi = len(formHaftaliksayi)

    DestekTalebiKayitlarHaftalikuser = DestekTalebiKayit.objects.filter(DestekTalebiBaslamaTarihi__range=[Haftalikenddate, baslangic],DestekTalebiAktif=True).values(
        'DestekTalebiUser').annotate(total=Count("DestekTalebiUser")).order_by('DestekTalebiUser')[::1]

    DestekTalebiKayitlarhaftaliksayisi = DestekTalebiKayit.objects.filter(DestekTalebiBaslamaTarihi__range=[Haftalikenddate, baslangic],DestekTalebiAktif=True).values(
        'DestekTalebiBaslamaTarihi').annotate(total=Count("DestekTalebiBaslamaTarihi")).order_by('DestekTalebiBaslamaTarihi')[::1]
    DestekTalebiKayitlarhaftaliksayisiuzunluk = len(DestekTalebiKayitlarhaftaliksayisi)

    DestekTalebiKayitlarHaftalik1 = DestekTalebiKayit.objects.filter(DestekTalebiBaslamaTarihi__range=[Haftalikenddate, baslangic],DestekTalebiAktif=True).values(
        'DestekTalebiBaslamaTarihi').annotate(total=Count("DestekTalebiBaslamaTarihi")).order_by('DestekTalebiBaslamaTarihi')[::1]
    formHaftaliksayi1 = DestekTalebiKayit.objects.filter(DestekTalebiBaslamaTarihi__range=[Haftalikenddate, baslangic],DestekTalebiAktif=True)
    DestekTalebiKayitlarHaftaliksayi1 = len(formHaftaliksayi1)
    
    DestekTalebiKayitlarGunluk = DestekTalebiKayit.objects.filter(DestekTalebiBaslamaTarihi__range=[startdate, baslangic],DestekTalebiAktif=True).values(
        'DestekTalebiKurum').annotate(total=Count("DestekTalebiKurum")).order_by('DestekTalebiKurum')[::1]
    formGunluksayi = DestekTalebiKayit.objects.filter(DestekTalebiBaslamaTarihi__range=[startdate, baslangic], DestekTalebiAktif=True)
    DestekTalebiKayitlarGunluksayi = len(formGunluksayi)


    kisilers = Kisi.objects.filter(KisiAktif=True)
    kurumlars = Kurumlar.objects.filter(KurumAktif=True)
    kurumBirimis = KurumBirimi.objects.filter(BirimAktif=True)

    NDestekTalebiKisiler = DestekTalebiKayit.objects.filter(DestekTalebiAktif=True).values('DestekTalebiKisi').annotate(
        total=Count("DestekTalebiKisi")).order_by('-DestekTalebiKisi')[:10][::-1]
    NDestekTalebiKayitlar = DestekTalebiKayit.objects.filter(DestekTalebiAktif=True).values('DestekTalebiKurum','DestekTalebiBirim').annotate(
        total=Count("DestekTalebiKurum")).order_by('-DestekTalebiKurum')[:10][::-1]
    NDestekTalebiKayitlartoplam = DestekTalebiKayit.objects.filter(DestekTalebiAktif=True).values(
        'DestekTalebiKurum').annotate(total=Count("DestekTalebiKurum")).order_by('-DestekTalebiKurum')[:10][::-1]
    Nkisilers = Kisi.objects.filter(KisiAktif=True)
    Nkurumlars = Kurumlar.objects.filter(KurumAktif=True)
    Nkullanici = User.objects.filter(is_active=True)
    NkurumBirimis = KurumBirimi.objects.filter(BirimAktif=True)

    
#----------------

    master_data_frame_kullanici = pd.DataFrame(Nkullanici)
    master_data_frame = pd.DataFrame(DestekTalebiKayitlarHaftalikuser)
    y = master_data_frame['DestekTalebiUser']
    x = master_data_frame["total"]
    print(master_data_frame_kullanici)

#--------------------
    #y = [1,2,3,4,5,6]
    #x = [21,23,26,27,12,13]
    plt.figure(figsize=(6, 6))
    plt.title('haftalık Kullanıcı dağılım')
    plt.plot(y, x)
    plt.xlabel('Kullanıcı')
    plt.ylabel('gelen çağrı')
    plt.grid(True)
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri=urllib.parse.quote(string)

#--------------------

    master_data_frame_date = pd.DataFrame(DestekTalebiKayitlarhaftaliksayisi)
    k = master_data_frame_date["DestekTalebiBaslamaTarihi"]
    l = master_data_frame_date["total"]
    print(master_data_frame_date)

    #print(master_data_frame_date[["DestekTalebiBaslamaTarihi","total"]])
    #print(master_data_frame_date["total"])
    #print(Nkullanici)

#--------------------
    #k = [1,2,3,4,5,6]
    #l = [21,23,26,27,12,13]
    plt.figure(figsize=(6, 6))
    plt.title('haftalık Günlük Dağılım')
    plt.plot(k, l)
    plt.xlabel('Günler')
    plt.ylabel('gelen çağrı')
    plt.grid(True)
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri1=urllib.parse.quote(string)




#--------------------

    return render(request, "TLP/TLPDestekTalebiIstatistik.html", {"DestekTalebiKayitlar": DestekTalebiKayitlar,
                                                                  "kurumlars": kurumlars,
                                                                  "kurumBirimis": kurumBirimis,
                                                                  "DestekTalebiKayitlartoplam": DestekTalebiKayitlartoplam,
                                                                  "DestekTalebiKisiler": DestekTalebiKisiler,
                                                                  "kisilers": kisilers,
                                                                  "NDestekTalebiKayitlar": NDestekTalebiKayitlar,
                                                                  "Nkurumlars": Nkurumlars,
                                                                  "NkurumBirimis": NkurumBirimis,
                                                                  "NDestekTalebiKayitlartoplam": NDestekTalebiKayitlartoplam,
                                                                  "NDestekTalebiKisiler": NDestekTalebiKisiler,
                                                                  "Nkisilers": Nkisilers,
                                                                  "Nbaslangic": startdate,
                                                                  "Nbitis":enddate,
                                                                  "Haftalikenddate":Haftalikenddate,
                                                                  "Aylikenddate":Aylikenddate,
                                                                  "DestekTalebiKayitlartoplamsayi": DestekTalebiKayitlartoplamsayi,
                                                                  "DestekTalebiKayitlarAylik":DestekTalebiKayitlarAylik,
                                                                  "DestekTalebiKayitlarAylikSayi":DestekTalebiKayitlarAyliksayi,
                                                                  "DestekTalebiKayitlarHaftalik": DestekTalebiKayitlarHaftalik,
                                                                  "DestekTalebiKayitlarHaftaliksayi": DestekTalebiKayitlarHaftaliksayi,
                                                                  "DestekTalebiKayitlarGunluk":DestekTalebiKayitlarGunluk,
                                                                  "DestekTalebiKayitlarGunluksayi":DestekTalebiKayitlarGunluksayi,
                                                                  "data":uri,
                                                                  "data1":uri1,
                                                                  "DestekTalebiKayitlarhaftaliksayisi":DestekTalebiKayitlarhaftaliksayisi,
                                                                  "DestekTalebiKayitlarHaftalikuser":DestekTalebiKayitlarHaftalikuser,
                                                                  "Nkullanici":Nkullanici,})


# -------------- Profil işlemleri -------------------


@xframe_options_sameorigin
@login_required(login_url="user:login")
def TLPUserprofil(request):
    if request.method == 'POST':
        form = UserEkleForm(data=request.POST, instance=request.user)
        update = form.save(commit=False)
        update.user = request.user
        update.save()
        messages.success(request, "Başarıyla Günceleme Yaptınız...")
    else:
        form = UserEkleForm(instance=request.user)
        messages.info(request, "Günceleme Yapılmadı...")
    return render(request, "TLP/Userprofil.html", {"form": form})


def TLPUserPasswordChange(request):
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
    return render(request, 'TLP/UserPasswordChange.html', {'form': form})

@xframe_options_sameorigin
@login_required(login_url="user:login")
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="cagrikayitlistesi.csv"'
    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    writer.writerow(["id","DestekTalebiBaslamaTarihi","DestekTalebiUygulama", "DestekTalebiKonu","DestekTalebiTuruAdi", "DestekTalebiKurum", "DestekTalebiBirim", "DestekTalebiKisi","DestekTalebiKisiTelefon","DestekTalebiTfsId","DestekTalebiDurumu","DestekTalebiAciklama"])
    cagrikayits = DestekTalebiKayit.objects.filter(DestekTalebiAktif=True, ).select_related('Uygulama','Kurumlar','KurumBirimi','DestekTalebiTuru').values_list("id","DestekTalebiBaslamaTarihi","DestekTalebiUygulama__UygulamaAdi", "DestekTalebiKonu","DestekTalebiTuruAdi__DestekTalebiAdi", "DestekTalebiKurum__KurumAdi", "DestekTalebiBirim__BirimAdi", "DestekTalebiKisi","DestekTalebiKisiTelefon","DestekTalebiTfsId","DestekTalebiDurumu","DestekTalebiAciklama")
    for cagrikayit in cagrikayits:
        writer.writerow(cagrikayit)    
    return response

@xframe_options_sameorigin
@login_required(login_url="user:login")
def export_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="cagrikayit.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('CagriKayitListesi')
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ["id","DestekTalebiBaslamaTarihi","DestekTalebiUygulama", "DestekTalebiKonu","DestekTalebiTuruAdi","DestekTalebiVeren","DestekTalebiKurum", "DestekTalebiBirim", "DestekTalebiKisi","DestekTalebiKisiTelefon","DestekTalebiTfsId","DestekTalebiDurumu","DestekTalebiAciklama"]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows = DestekTalebiKayit.objects.filter(DestekTalebiAktif=True, ).select_related('Uygulama','Kurumlar','KurumBirimi','DestekTalebiTuru').values_list("id","DestekTalebiBaslamaTarihi","DestekTalebiUygulama__UygulamaAdi", "DestekTalebiKonu","DestekTalebiTuruAdi__DestekTalebiAdi","DestekTalebiKategori__KategoriAdi", "DestekTalebiKurum__KurumAdi", "DestekTalebiBirim__BirimAdi", "DestekTalebiKisi","DestekTalebiKisiTelefon","DestekTalebiTfsId","DestekTalebiDurumu","DestekTalebiAciklama")
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response
