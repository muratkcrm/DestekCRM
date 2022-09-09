from datetime import datetime
from django.shortcuts import render, HttpResponse,redirect, get_object_or_404,HttpResponseRedirect
from .forms import LoginForm, UserEkleForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseForbidden
from django.core.cache import cache
from django.contrib.sessions.models import Session



# Create your views here.

def UserPasswordChange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, '"Parola Değişimi Yapıldı...."!')
        else:
            messages.info(request, "Parola Değişmedi...")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, '../templates/TLP/UserPasswordChange.html', {'form': form})

def loginUser(request):
    form =  LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request, "kullanıcı adı veya parola hatalı")
            return render(request,"login.html",context)
        messages.success(request,"Başarıyla Giriş yaptınız...")
        login(request,user)
        return redirect ("index")
    return render(request,"login.html",context)


@login_required(login_url="user:login")
def logoutUser(request):
    Session.objects.all().delete()
    logout(request)
    cache.clear()
    return redirect("/user/login")

@login_required(login_url="user:login")
def Userprofil(request):
    if request.method == 'POST':
        form = UserEkleForm(data=request.POST, instance=request.user)
        update = form.save(commit=False)
        update.user = request.user
        update.save()
        messages.success(request, "Başarıyla Günceleme Yaptınız...")
    else:
        form = UserEkleForm(instance=request.user)
    return render(request, "../templates/TLP/Userprofil.html", {"form" : form})