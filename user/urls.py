from django.contrib import admin
from django.urls import path,include
from . import views
from django.urls import include
from django.urls import re_path as url
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

app_name = "user"

urlpatterns = [
    path('login/',views.loginUser,name = "login"),
    path('logout/',views.logoutUser,name = "logout"),
    path('Userprofil/', views.Userprofil, name= "Userprofil"),
    url(r'^UserPasswordChange/',views.UserPasswordChange,name = "UserPasswordChange"),
]
