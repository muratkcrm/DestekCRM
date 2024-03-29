# Generated by Django 4.0.3 on 2022-03-26 21:36

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PerTakipKayit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('PTKTckimlik', models.CharField(blank=True, max_length=250, verbose_name='Tc Kimlik No')),
                ('PTKAdiSoyadi', models.CharField(blank=True, max_length=250, verbose_name='Personel Adı-Soyadı')),
                ('PTKIseGiristarihi', models.DateField(blank=True, verbose_name='İşe Giriş Tarihi :')),
                ('PTKIseCikistarihi', models.DateField(blank=True, null=True, verbose_name='İşe Çıkış Tarihi :')),
                ('PTKAdres', models.CharField(blank=True, max_length=250, null=True, verbose_name='Adres')),
                ('PTKIl', models.CharField(blank=True, max_length=50, null=True, verbose_name='İl')),
                ('PTKIlce', models.CharField(blank=True, max_length=50, null=True, verbose_name='İlçe')),
                ('PTKEmail', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('PTKTelefon', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefon')),
                ('PTKGorevi', models.CharField(blank=True, max_length=50, null=True, verbose_name='Personel Görevi')),
                ('PTKAciklama', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Açıklama')),
                ('PTKDosya', models.FileField(blank=True, null=True, upload_to='Dosya/Not/', verbose_name='Not ile ilgili dosya ekle')),
                ('PTKAktif', models.BooleanField(default=True, verbose_name='silmek için Onayı kaldırın..!!!')),
                ('PTKDurumu', models.CharField(choices=[('Çalışıyor', 'Çalışıyor'), ('Ayrıldı', 'Ayrıldı')], default='Çalışıyor', max_length=50, verbose_name='Çalışıyor Mu ?')),
                ('PTKOluşturmatarihi', models.DateTimeField(auto_now_add=True, null=True)),
                ('PTKModifiyeTarihi', models.DateTimeField(blank=True, editable=False, null=True)),
            ],
            options={
                'verbose_name_plural': 'Personel kayıt girişi',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PTKFirma',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('PTKFirmaTarihi', models.DateTimeField(auto_now_add=True)),
                ('PTKFirmaAdi', models.CharField(default='', max_length=250, verbose_name='Firma Adını giriniz')),
                ('PTKFirmaAciklama', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Firma Bilgisi')),
                ('PTKFirmaAktif', models.BooleanField(default=True, verbose_name='silmek için Onayı kaldırın..!!!')),
                ('PTKFirmaUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PTKDuyurular',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('PTKDuyuruTarihi', models.DateTimeField(auto_now_add=True)),
                ('PTKDuyuruBaslik', models.CharField(default='', max_length=250, verbose_name='Duyurunun Konusu')),
                ('PTKDuyuruAciklama', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Duyuru Metni')),
                ('PTKDuyuruAktif', models.BooleanField(default=True, verbose_name='silmek için Onayı kaldırın..!!!')),
                ('PTKDuyuruUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'PTKDuyurular',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PerTakipNotlar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('PerTakipNotlarKonu', models.CharField(max_length=50, verbose_name='Konu')),
                ('PerTakipMetin', ckeditor.fields.RichTextField(help_text='Çağrı ile İlgili Tüm Notlarınızı ekleyebilirsiniz..', max_length=2000, null=True, verbose_name='İçerik')),
                ('PerTakipOlusturmaTarihi', models.DateTimeField(auto_now_add=True, null=True)),
                ('PerTakipNotDosya', models.FileField(blank=True, null=True, upload_to='Notlar/', verbose_name='Çağrı Notlarına Dosya Ekle')),
                ('PerTakipNotAktif', models.BooleanField(default=True, verbose_name='silmek için Onayı kaldırın..!!!')),
                ('PerTakipKayit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='DestekTalebiNotlar', to='PerTakip.pertakipkayit')),
                ('PerTakipNotUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Personel Notları',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='pertakipkayit',
            name='PTKFirmaAdi',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='PerTakip.ptkfirma', verbose_name='Hangi Firmada'),
        ),
        migrations.AddField(
            model_name='pertakipkayit',
            name='PTKKayitUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Talebi Açan Kullanıcı'),
        ),
        migrations.CreateModel(
            name='PerIzinHakedis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('PerIzinHakedisDonemi', models.CharField(blank=True, default='2022', max_length=10, null=True, verbose_name='Personel İzin Hakediş Dönemi :')),
                ('PerIzinHakedistarihi', models.DateField(blank=True, null=True, verbose_name='Personel İzin Hakediş Tarihi :')),
                ('PerIzinHakedilenSure', models.FloatField(blank=True, null=True)),
                ('PerIzinHakedisOluşturmatarihi', models.DateTimeField(auto_now_add=True, null=True)),
                ('PerIzinHakedisModifiyeTarihi', models.DateTimeField(blank=True, editable=False, null=True)),
                ('PerIzinHakedisAktif', models.BooleanField(default=True, verbose_name='silmek için Onayı kaldırın..!!!')),
                ('PerIzinHakedisUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('PerTakipKayit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PerTakip.pertakipkayit')),
            ],
            options={
                'verbose_name_plural': 'Personel Hakedilen İzin',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PerIzinDurum',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('PerIzinDonemi', models.CharField(blank=True, default='2022', max_length=10, null=True, verbose_name='Personel Kullanılan İzin Dönemi :')),
                ('PerIzinBaslatarihi', models.DateField(blank=True, verbose_name='Personel İzin Başlangıç Tarihi :')),
                ('PerIzinBitistarihi', models.DateField(blank=True, null=True, verbose_name='Personel İzin Bitiş Tarihi :')),
                ('PerIzinKonu', models.CharField(max_length=50, verbose_name='İzin Nedeni')),
                ('PerIzinSuresi', models.FloatField(blank=True, null=True)),
                ('PerIzinOnayVeren', models.CharField(default='Oktay Bey', max_length=50, verbose_name='İzin Onaylayan')),
                ('PerIzinOluşturmatarihi', models.DateTimeField(auto_now_add=True, null=True)),
                ('PerIzinModifiyeTarihi', models.DateTimeField(blank=True, editable=False, null=True)),
                ('PerIzinDosya', models.FileField(blank=True, null=True, upload_to='Izinler/', verbose_name='İzin Formu Dosya ya Ekle')),
                ('PerIzinAktif', models.BooleanField(default=True, verbose_name='silmek için Onayı kaldırın..!!!')),
                ('PerIzinUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('PerTakipKayit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PerTakip.pertakipkayit')),
            ],
            options={
                'verbose_name_plural': 'Personel izin girişi',
                'ordering': ['-id'],
            },
        ),
    ]
