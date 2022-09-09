"""destek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.authtoken import views as appviews
from django.urls import re_path as url
from django.urls import include
from rest_framework.authtoken import views

from . import  views

app_name = "TalepYonetimi"
app_name = "Satis"
app_name = "Yonetim"
app_name = "app"
app_name = "PerTakip"

urlpatterns = [
    path('Yonetim/', include("Yonetim.urls")),
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('user/', include("user.urls")),
    path('app/', include("app.urls")),
    path('TalepYonetimi/', include("TalepYonetimi.urls")),
    path('Satis/', include("Satis.urls")),
    path('PerTakip/', include("PerTakip.urls")),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^user/', include('rest_framework.urls')),
    path('app/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('app/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('app/users/api-token-auth/', appviews.obtain_auth_token, name='app-token-auth'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)