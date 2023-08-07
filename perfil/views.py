from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants

from perfil.models import Conta




def home (request):
    return render(request, 'home.html')

def gerenciar(request):
    return render(request, 'gerenciar.html')

def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.FILES.get('icone')
    
    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
        return redirect('/perfil/gerenciar')
    
    conta = Conta(
        apelido = apelido, 
        banco = banco,
        tipo = tipo,
        valor = valor,
        icone = icone   
        
    )
    
    conta.save()
    messages.add_message(request, constants.SUCCESS, 'Cadastro feito com sucesso!')
    return redirect('/perfil/gerenciar')