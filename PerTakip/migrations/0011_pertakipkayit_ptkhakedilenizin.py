# Generated by Django 4.0.4 on 2022-05-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PerTakip', '0010_alter_perizindurum_perizinsuresigun_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pertakipkayit',
            name='PTKHakedilenIzin',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Hakedilen İzin Süresi Gün'),
        ),
    ]
