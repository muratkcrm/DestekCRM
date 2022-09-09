from django.contrib.auth.models import User, Group
from openpyxl.pivot.cache import Groups
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from TalepYonetimi.models import Kategori, DestekTalebiKayit, DestekTalebiTuru, Kurumlar


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "email","password"]

    validators = [
        UniqueTogetherValidator(
            queryset=User.objects.all(),
            fields=['username', 'email']
        )
    ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ["id", "KategoriAdi", "KategoriAciklama"]

class DestekTalebiKurumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kurumlar
        fields = ["id", "KurumAdi", "KurumAktif"]


class DestekTalepSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestekTalebiKayit
        fields = ["id", "DestekTalebiUygulama", "DestekTalebiUser", "DestekTalebiTuruAdi", "DestekTalebiKonu",
                  "DestekTalebiDurumu", "DestekTalebiAciklama", "DestekTalebiKurum", "DestekTalebiBirim",
                  "DestekTalebiKisi"]


class DestekTalebiTuruSerializer(serializers.ModelSerializer):
    TuruAdi = serializers.StringRelatedField(many=True)

    class Meta:
        model = DestekTalebiTuru
        fields = ['DestekTalebiAdi', 'DestekTalebiAciklama', 'TuruAdi']

