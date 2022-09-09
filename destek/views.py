from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url="user:login")
def index(request):
    pass
    return render(request,"index.html")
