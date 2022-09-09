from django.contrib import admin

from .models import DestekTalebiKayit
from .models import DestekTalebiNotlar
from .models import DestekTalebiTuru
from .models import Duyurular
from .models import Kategori
from .models import Kisi
from .models import KurumBirimi
from .models import Kurumlar
from .models import Uygulama


# Register your models here.

admin.site.register(DestekTalebiNotlar)


@admin.register(DestekTalebiKayit)
class DestekTalebiDestekAdmin(admin.ModelAdmin):
    list_display = ["id", "DestekTalebiUygulama", "DestekTalebiTuruAdi", "DestekTalebiUser", "DestekTalebiBirim",
                    "DestekTalebiDurumu"]
    list_display_links = ["id","DestekTalebiUygulama","DestekTalebiTuruAdi","DestekTalebiUser","DestekTalebiBirim","DestekTalebiDurumu"]
    search_fields = ["DestekTalebiKonu","DestekTalebiAciklama"]

    class Meta:
        model = DestekTalebiKayit


@admin.register(DestekTalebiTuru)
class DestekTalebiTuruAdmin(admin.ModelAdmin):

    list_display = ["id", "DestekTalebiAdi"]
    list_display_links = ["id", "DestekTalebiAdi"]
    search_fields = ["DestekTalebiAdi"]

    class Meta:
        model = DestekTalebiTuru

@admin.register(Uygulama)
class UygulamaAdmin(admin.ModelAdmin):

    list_display = ["id", "UygulamaAdi","UygulamaAciklama"]
    list_display_links = ["id", "UygulamaAdi"]
    search_fields = ["UygulamaAdi"]

    class Meta:
        model = Uygulama


@admin.register(Kurumlar)
class KurumlarAdmin(admin.ModelAdmin):

    list_display = ["id" ,"KurumAdi","KurumIl"]
    list_display_links = ["id", "KurumAdi", "KurumIl"]
    search_fields = ["KurumAdi"]

    class Meta:
        model = Kurumlar


@admin.register(KurumBirimi)
class KurumBirimiAdmin(admin.ModelAdmin):

    list_display = ["id", "BirimAdi"]
    list_display_links = ["id", "BirimAdi"]
    search_fields = ["BirimAdi"]
    list_filter = ["BirimAdi"]

    class Meta:
        model = KurumBirimi
       

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):

    list_display = ["id", "KategoriAdi"]
    list_display_links = ["id", "KategoriAdi"]

    class Meta:
        model = Kategori


@admin.register(Kisi)
class KisiAdmin(admin.ModelAdmin):

    list_display = ["KisiAdiSoyadi","KurumAdi","KisiBirimAdi","KisiTelefon","KisiEmail"]
    list_display_links = ["KisiAdiSoyadi","KurumAdi","KisiBirimAdi", "KisiTelefon", "KisiEmail"]
    search_fields = ["KisiAdiSoyadi","KurumAdi","KisiBirimAdi"]
    list_filter = [ "KurumAdi","KisiBirimAdi"]
    class Meta:
        model = Kisi
        

@admin.register(Duyurular)
class DuyurularAdmin(admin.ModelAdmin):

    list_display = ["id", "DuyuruUser","DuyuruTarihi","DuyuruBaslik","DuyuruAciklama"]
    list_display_links = ["id", "DuyuruUser","DuyuruTarihi","DuyuruBaslik","DuyuruAciklama"]

    class Meta:
        model = Duyurular
