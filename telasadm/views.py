from django.shortcuts import render,redirect
from rifas.models import skin
from rifas.models import rifa

def cd_skin(request):
    if request.method == 'POST':
        categoria =  request.POST['categoria']
        nome =  request.POST['nome']
        valor =  request.POST['valor']
        link =  request.POST['link']
        skins = skin.objects.create(nome=nome,categoria=categoria,valor=valor,link=link)     
        skins.save()
        return render(request,'cd_skin.html')

    return render(request,'cd_skin.html')

def cd_rifa(request):
    if request.method == 'POST':
        valor_total =  request.POST['valor_total']
        num_entradas =  request.POST['num_entradas']
        valor_entrada =  request.POST['valor_entrada']
        
        data_inicial =  request.POST['data_inicial']
        data_final =  request.POST['data_final']
        id_skin =  request.POST['id_skin']
        ativa =  request.POST['ativa']
        skins = skin.objects.get(id=int(id_skin))
        participantes = "{"
        for i in range(1,int(num_entradas)+1):
            participantes += "'" + str(i) + "':" + "'',"

        participantes = participantes[0:-1]
        participantes += "}"  
        print(participantes)
        rifas = rifa.objects.create(valor_total=valor_total,num_entradas=num_entradas,valor_entrada=valor_entrada,participantes=participantes,data_inicial=data_inicial,data_final=data_final,skin=skins,ativa=ativa)     
        rifas.save()
        return render(request,'cd_rifa.html')




    return render(request,'cd_rifa.html')
