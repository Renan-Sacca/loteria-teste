from django.shortcuts import render,redirect
from rifas.models import rifa
from rifas.models import skin


def index(request):
    
    rifas = rifa.objects.all()
    dados={
        'rifa' : rifas,
    }
    print(dados)
    if request.user.is_authenticated:
        return render(request,'dashboard.html',dados)
    else:
        return render(request,'index.html', dados)

    

