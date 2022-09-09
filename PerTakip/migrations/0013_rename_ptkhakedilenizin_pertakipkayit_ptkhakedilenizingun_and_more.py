# Generated by Django 4.0.4 on 2022-05-28 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PerTakip', '0012_pertakipkayit_ptkhakedilenizinyil'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pertakipkayit',
            old_name='PTKHakedilenIzin',
            new_name='PTKHakedilenIzinGun',
        ),
        migrations.AddField(
            model_name='pertakipkayit',
            name='PTKIzinSuresiGun',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Kullanılan İzin Süresi Gün'),
        ),
        migrations.AddField(
            model_name='pertakipkayit',
            name='PTKIzinSuresiSaat',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Kullanılan İzin Süresi Saat'),
        ),
    ]