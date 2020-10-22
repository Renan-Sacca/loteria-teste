from django.shortcuts import render,redirect
from rifas.models import rifa
from login.models import Profile
from django.contrib.auth.models import User
from django.contrib import auth



def rifas(request,valor):
    rifas = rifa.objects.filter(id=valor)
    profiles = Profile.objects.filter(user=request.user.id)
    print(profiles)
    dados = {
        'rifa' : rifas,
        'profiles': profiles,
    }
    
    return render(request,'rifas.html',dados)
