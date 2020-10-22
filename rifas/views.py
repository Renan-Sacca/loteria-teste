from django.shortcuts import render,redirect
from rifas.models import rifa




def rifas(request,valor):
    rifas = rifa.objects.filter(id=valor)
    
    dados = {
        'rifa' : rifas,
    }
    
    return render(request,'rifas.html',dados)
