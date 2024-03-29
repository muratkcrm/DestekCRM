# Generated by Django 3.1.4 on 2020-12-01 07:32

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
            name='WfaMobilUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wfauser', models.CharField(max_length=20)),
                ('wfapassword', models.CharField(max_length=20)),
                ('wfaMobilUserAktif', models.BooleanField(default=True, verbose_name='silmek için Onayı kaldırın..!!!')),
                ('wfakullanici', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]
