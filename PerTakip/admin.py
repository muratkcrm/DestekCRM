from pyexpat import model
from django.contrib import admin
from import_export.admin import ExportActionMixin

from .models import PerIzinHakedis, PerTakipKayit, PTKDuyurular, PerTakipNotlar, PTKFirma, PerIzinDurum


# Register your models here.

#admin.site.register(PerTakipKayit)

@admin.register(PerTakipKayit)
class PerTakipKayitAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["id", "PTKTckimlik","PTKAdiSoyadi","PTKIseGiristarihi","PTKIseCikistarihi","PTKFirmaAdi","PTKDurumu"]
    list_display_links = ["id", "PTKTckimlik","PTKAdiSoyadi","PTKIseGiristarihi","PTKIseCikistarihi","PTKFirmaAdi","PTKDurumu"]
    search_fields = ["id", "PTKTckimlik","PTKAdiSoyadi","PTKIseGiristarihi","PTKIseCikistarihi","PTKFirmaAdi","PTKDurumu"]
    class Meta:
        model = PerTakipKayit



@admin.register(PerTakipNotlar)
class PerTakipNotlarAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["id", "PerTakipKayit","PerTakipNotlarKonu","PerTakipOlusturmaTarihi","PerTakipNotUser","PerTakipNotAktif"]
    list_display_links = ["id", "PerTakipKayit","PerTakipNotlarKonu","PerTakipOlusturmaTarihi","PerTakipNotUser","PerTakipNotAktif"]
    search_fields = ["id", "PerTakipKayit","PerTakipNotlarKonu","PerTakipOlusturmaTarihi","PerTakipNotUser","PerTakipNotAktif"]
    class Meta:
        model = PerTakipNotlar



@admin.register(PTKDuyurular)
class PTKDuyurularAdmin(ExportActionMixin, admin.ModelAdmin):
    class Meta:
        model = PTKDuyurular


@admin.register(PTKFirma)
class PTKFirmaAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["id", "PTKFirmaAdi","PTKFirmaAciklama","PTKFirmaAktif","PTKFirmaUser"]
    list_display_links = ["id", "PTKFirmaAdi","PTKFirmaAciklama","PTKFirmaAktif","PTKFirmaUser"]
    search_fields = ["id", "PTKFirmaAdi","PTKFirmaAciklama","PTKFirmaAktif","PTKFirmaUser"]
    class Meta:
        model = PerTakipNotlar

@admin.register(PerIzinDurum)
class PerIzinDurumAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["id","PerTakipKayit","PerIzinBaslatarihi","PerIzinBitistarihi","PerIzinKonu","PerIzinSuresiGun","PerIzinSuresiSaat","PerIzinOnayVeren"]
    list_display_links = ["id","PerTakipKayit","PerIzinBaslatarihi","PerIzinBitistarihi","PerIzinKonu","PerIzinSuresiGun","PerIzinSuresiSaat","PerIzinOnayVeren"]
    search_fields = ["id","PerTakipKayit","PerIzinBaslatarihi","PerIzinBitistarihi","PerIzinKonu","PerIzinSuresiGun","PerIzinSuresiSaat","PerIzinOnayVeren"]
    class Meta:
        model = PerIzinDurum

@admin.register(PerIzinHakedis)
class PerIzinHakedisAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["id","PerTakipKayit","PerIzinHakedisDonemi","PerIzinHakedistarihi","PerIzinHakedilenSure"]
    list_display_links = ["id","PerTakipKayit","PerIzinHakedisDonemi","PerIzinHakedistarihi","PerIzinHakedilenSure"]
    search_fields = ["id","PerTakipKayit","PerIzinHakedisDonemi","PerIzinHakedistarihi","PerIzinHakedilenSure"]
    class Meta:
        model = PerIzinHakedis
