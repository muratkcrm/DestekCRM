from ckeditor.fields import RichTextField
from django.utils import timezone
#from smart_selects.db_fields import *
from smart_selects.db_fields import ChainedForeignKey
from django.db import models
#from djongo import models
from mongoengine import *


# Create your models here.


class DestekTalebiKayit(models.Model):
    id = models.AutoField(primary_key=True)
    Durum_CHOICES = (('Kapalı', 'Kapalı'),('Açık', 'Açık'))

    DestekTalebiUygulama = models.ForeignKey("Uygulama", default=1, on_delete=models.SET_NULL, null=True,
                                             verbose_name="Uygulama Adı")
    DestekTalebiUser = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, blank=True,
                                         verbose_name="Talebi Açan Kullanıcı", related_name='Kullanici')
    DestekTalebiKonu = models.CharField(max_length=100, verbose_name="Talep Konusu")
    DestekTalebiTuruAdi = models.ForeignKey("DestekTalebiTuru", default=1, on_delete=models.SET_NULL, null=True,
                                            verbose_name="Talep Türü", related_name='TuruAdi')
    DestekTalebiKategori = models.ForeignKey("Kategori", default=1,on_delete=models.SET_NULL, null=True, verbose_name="Destek Kaynağı")
    DestekTalebiKurum = models.ForeignKey("Kurumlar", on_delete=models.SET_NULL, null=True, verbose_name="Kurum Adı")
    DestekTalebiBirim = ChainedForeignKey("KurumBirimi", on_delete=models.DO_NOTHING,verbose_name="Birim Adı",
                                      chained_field="DestekTalebiKurum",
                                      chained_model_field="KurumAdi",
                                      show_all=False,
                                      auto_choose = True,
                                      sort=True)
    DestekTalebiKisi = models.CharField(max_length=100,null=True,blank=True ,verbose_name="Talep Eden Kişi")
    #DestekTalebiKisi = ChainedForeignKey("Kisi", on_delete=models.DO_NOTHING,verbose_name="Talep Eden Kişi",
    #                                  chained_field="DestekTalebiKurum",
    #                                  chained_model_field="KurumAdi",
    #                                  show_all=False,
    #                                  auto_choose = True,
    #                                  sort=True)
    DestekTalebiKisiTelefon = models.CharField(max_length=100,null=True,blank=True , verbose_name="İletişim")
    DestekTalebiDurumu = models.CharField(default=1, choices=Durum_CHOICES, max_length=50, verbose_name="Talep Durumu")
    #DestekTalebiAciklama = RichTextField()
    DestekTalebiAciklama = models.TextField()
    DestekTalebiDosya = models.FileField(blank=True, null=True, verbose_name="Talep ile ilgili dosya ekle", upload_to='Dosya/')
    DestekTalebiBaslamaTarihi = models.DateField(auto_now_add=True, null=True, blank=True)
    DestekTalebiKayitTarihi = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    DestekTalebiKapanmaTarihi = models.DateTimeField(auto_now=True, null=True, blank=True)
    DestekTalebiAktif = models.BooleanField(default=True, verbose_name="silmek için Onayı kaldırın..!!!")
    DestekTalebiTfsId = models.CharField(max_length=100,null=True,blank=True , verbose_name="Tfs Id")


    class Meta:
        ordering = ['-id']

    def get_DestekTalebiDosya(self):
        if self.DestekTalebiDosya:
            return self.DestekTalebiDosya.url
        else:
            return None

    def __str__(self):
        return ('%s : %s')%(self.DestekTalebiKonu, self.DestekTalebiAciklama)

    def __str__(self):
        return "%s" % (self.id)



class DestekTalebiNotlar(models.Model):
    id = models.AutoField(primary_key=True)
    DestekTalebiKayit = models.ForeignKey(DestekTalebiKayit, on_delete=models.SET_NULL, null=True, related_name="DestekTalebiNotlar")
    DestekTalebiNotlarKonu = models.CharField( max_length=50, verbose_name="Konu")
    Metin = RichTextField(max_length=2000, null=True, blank=False, verbose_name="İçerik",
                          help_text="Çağrı ile İlgili Tüm Notlarınızı ekleyebilirsiniz..")
    OlusturmaTarihi = models.DateTimeField(auto_now_add=True, null=True)
    DestekTalebiNotUser = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, blank=True)
    DestekTalebiNotDosya = models.FileField(blank=True, null=True, verbose_name="Çağrı Notlarına Dosya Ekle",upload_to='Notlar/')
    DestekTalebiNotAktif = models.BooleanField(default=True, verbose_name="silmek için Onayı kaldırın..!!!")

    class Meta:
        verbose_name_plural = 'Cağrı Notları'
        ordering = ['-id']

    def __str__(self):
        return self.DestekTalebiNotlarKonu



class DestekTalebiTuru(models.Model):
    id = models.AutoField(primary_key=True)
    DestekTalebiAdi = models.CharField(max_length=30)
    DestekTalebiAciklama = models.CharField(max_length=150)
    DestekTalebiAktif = models.BooleanField(default=True, verbose_name="silmek için Onayı kaldırın..!!!")

    def __str__(self):
        return self.DestekTalebiAdi

    class Meta:
        ordering = ['id']



class Uygulama(models.Model):
    id = models.AutoField(primary_key=True)
    UygulamaAdi = models.CharField(max_length=30, verbose_name="Ürün/Modül Adı")
    UygulamaAciklama = models.CharField(max_length=150, verbose_name="Ürün/Modül Açıklama")
    UygulamaAktif = models.BooleanField(default=True, verbose_name="silmek için Onayı kaldırın..!!!")
    UygulamaCreated = models.DateTimeField(editable=False)
    UygulamaModified = models.DateTimeField()
    UygulamaUser = models.ForeignKey("auth.User", on_delete=models.CASCADE, default=1)
    UygulamaModifiedby = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True,
                                           related_name='modified_by')
    # -----------slug eklemek istendiğinde gerekli komutlar eklenmiştir.------
    #slug = models.SlugFields(unique=True, max_length=150, editable=False)
    #def get_slug(self):
    #    slug = slugify(self.UygulamaAdi.replace("ı","i"))
    #    unique = slug
    #    number = 1
    #    while Uygulama.objects.filter(slug = unique).exists():
    #        unique = '{}-{}'.format(slug, number)
    #        number +=1
    #    return unique

    def save(self, *args, **kwargs):
        if not self.id:
            self.UygulamaCreated = timezone.now()
        self.UygulamaModified = timezone.now()
        #self.slug = self.get_slug()
        return super(Uygulama, self).save(*args, **kwargs)

    def __str__(self):
        return self.UygulamaAdi
    class Meta:
        ordering = ['id']


class Kurumlar(models.Model):
    id = models.AutoField(primary_key=True)
    KurumAdi = models.CharField(max_length=250)
    KurumAdres = models.CharField(blank=True, null=True, max_length=250)
    KurumIl = models.CharField(blank=True, null=True, max_length=50)
    KurumEmail = models.EmailField(blank=True, null=True, )
    KurumYetkili = models.CharField(blank=True, null=True, max_length=150)
    KurumTelefon = models.CharField(blank=True, null=True, max_length=50)
    KurumAktif = models.BooleanField(default=True, verbose_name="silmek için Onayı kaldırın..!!!")
    KurumCreate = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.KurumAdi

    class Meta:
        ordering = ['id']



class KurumBirimi(models.Model):
    id = models.AutoField(primary_key=True)
    KurumAdi = models.ForeignKey(Kurumlar, on_delete=models.SET_NULL,null=True,related_name="kurumlar",help_text="Birimin üst kurum adı seçimi yapılır.")
    BirimAdi = models.CharField(max_length=250)
    BirimAdresi = models.CharField(blank=True, null=True, max_length=250)
    BirimEmail = models.EmailField(blank=True, null=True)
    BirimYetkili = models.CharField(blank=True, null=True, max_length=150)
    BirimTelefon = models.CharField(blank=True, null=True, max_length=50)
    BirimAktif = models.BooleanField(default=True, verbose_name="silmek için Onayı kaldırın..!!!")
    BirimCreate = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.BirimAdi

    class Meta:
        ordering = ['KurumAdi','BirimAdi','id']



class Kategori(models.Model):
    id = models.AutoField(primary_key=True)
    KategoriAdi = models.CharField( max_length=50, verbose_name="Kategori Adı")
    KategoriAciklama = models.CharField(blank=True, null=True, max_length=150, verbose_name="Kategori Açıklama")
    KategoriAktif = models.BooleanField(default=True, verbose_name="silmek için Onayı kaldırın..!!!")

    def __str__(self):
        return self.KategoriAdi

    class Meta:
        ordering = ['id']

class Kisi(models.Model):
    id = models.AutoField(primary_key=True)
    KisiAdiSoyadi = models.CharField(blank=False, null=False, max_length=250, verbose_name="Adı Soyadı")
    KurumAdi = models.ForeignKey(Kurumlar, on_delete=models.SET_NULL, null=True, verbose_name="Kurum Adı")
    KisiBirimAdi=ChainedForeignKey(KurumBirimi, on_delete=models.DO_NOTHING,verbose_name="Birim Adı",
                                                                chained_field="KurumAdi",
                                                                chained_model_field="KurumAdi",
                                                                show_all=False,
                                                                auto_choose=True,
                                                                sort=True)
    KisiTelefon = models.CharField(blank=True, null=True, max_length=50)
    KisiEmail = models.EmailField(blank=True, null=True, )
    KisiUser= models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, blank=True)
    KisiAktif = models.BooleanField(default=True, verbose_name="silmek için Onayı kaldırın..!!!")

    def __str__(self):
        return self.KisiAdiSoyadi

    class Meta:
        verbose_name_plural = 'Kişi Kayıtları'
        ordering = ['-id']


class Duyurular(models.Model):
    id = models.AutoField(primary_key=True)
    Duyurular_CHOICES = (('0','Hepsi'),('1', 'GorevTakip'), ('2', 'TalepYonetim'),('3','Satis'))

    DuyuruUser = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, blank=True)
    DuyuruTarihi = models.DateTimeField(auto_now_add=True)
    DuyuruBaslik = models.CharField(max_length=250, default="", verbose_name="Duyurunun Konusu")
    DuyuruAciklama = RichTextField(blank=True, null=True, verbose_name="Duyuru Metni")
    DuyuruUygulama = models.CharField(default=0, choices=Duyurular_CHOICES, max_length=50, verbose_name="Talep Durumu")
    DuyuruAktif = models.BooleanField(default=True, verbose_name="silmek için Onayı kaldırın..!!!")

    class Meta:
        verbose_name_plural = 'Duyurular'
        ordering = ['-id']

    def __str__(self):
        return self.DuyuruBaslik




