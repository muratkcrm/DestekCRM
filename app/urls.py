from django.conf import settings
from django.urls import include
from django.urls import re_path as url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path
from rest_framework import routers, serializers, viewsets

from . import views
from .views import UserRecordView, KategoriRecordView, GroupViewSet, DestekTalebiKurumlarView

app_name = "app"

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'kategori', views.KategoriViewSet)
router.register(r'TalebiKayit', views.DestekTalepViewSet)
router.register(r'DestekTalebiTuru', views.DestekTalebiTuruViewSet)
router.register(r'Kurumlar', views.DestekTalebiKurumlarViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    path('', include(router.urls)),
    path('user/', UserRecordView.as_view(), name='users'),
    path('kategori/', KategoriRecordView.as_view(), name='kategori'),
    path('kurumlar/', DestekTalebiKurumlarView.as_view(), name='kurumlar'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
