# sys.path.append('../')
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.utils import inspect
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from TalepYonetimi.models import Kategori, DestekTalebiKayit, DestekTalebiTuru, KurumBirimi, Kurumlar
from .serializers import UserSerializer, GroupSerializer, KategoriSerializer, DestekTalepSerializer, \
    DestekTalebiTuruSerializer, DestekTalebiKurumSerializer


class UserRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    permission_classes = [IsAdminUser]

    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'error': True,
                'error_msg': serializer.error_messages,
                'token': Token.key,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class KategoriRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    permission_classes = [IsAdminUser]

    def get(self, format=None):
        kategori = Kategori.objects.all()
        serializer = UserSerializer(kategori, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KategoriSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class DestekTalebiKurumlarView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    permission_classes = [IsAdminUser]

    def get(self, format=None):
        kurumlar = DestekTalebiKurumSerializer.objects.all()
        serializer = UserSerializer(kurumlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KategoriSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [IsAdminUser]
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = [IsAdminUser]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class KategoriViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = [IsAdminUser]

    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer


class DestekTalepViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = [IsAdminUser]
    queryset = DestekTalebiKayit.objects.filter(DestekTalebiAktif=True)
    serializer_class = DestekTalepSerializer


class DestekTalebiTuruViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = [IsAdminUser]
    queryset = DestekTalebiTuru.objects.filter(DestekTalebiAktif=True)
    serializer_class = DestekTalebiTuruSerializer



class DestekTalebiKurumlarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = [IsAdminUser]
    queryset = Kurumlar.objects.filter(KurumAktif=True)
    serializer_class = DestekTalebiKurumSerializer
