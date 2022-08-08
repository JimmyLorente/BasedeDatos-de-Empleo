from cmath import inf
import email
from urllib.request import Request
from django.shortcuts import render
from tasks import FormularioTrabajo

# Create your views here.

def contacto(request):
    if request.method=="POST":
        miFormulario=FormularioTrabajo(request.POST)

        if miFormulario.is_valid():

            infForm=miFormulario.cleaned_data

            send_mail(infForm['nombres'], infForm['telefono'], infForm['fecha'], infForm['describete'],
            infForm.get('email',''))
