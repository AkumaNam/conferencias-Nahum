
from typing import Text

from django import http
from app_registro.models import Participantes, Conferencia
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from telegram import Bot, chat # pip install python-telegram-bot

TOKEN = '1811443058:AAGltVkz7LLbXH1UG-RzEDonpjqj04EXj3g'
GROUP_ID = -503563314

bot = Bot(token=TOKEN)

@login_required()
def index(request):
     return render(request, 'registro/index.html')


@login_required
def participantes(request): 

     

     if request.method == 'POST':
          nombre = request.POST.get('nombre')
          apellido = request.POST.get('apellido')
          correo = request.POST.get('correo')
          twitter = request.POST.get('twitter')

          p = Participantes(nombre = nombre, apellido = apellido, correo = correo, twitter = twitter)
          p.save()

          msj = f'El participante {nombre} {apellido} ha sido registrado con exito.'
          
         


          # codigo para enviar un mensaje a un grupo de telegram

          try:
               bot.send_message(chat_id = GROUP_ID, text = msj)
          except Exception as e:
               msj += f'<br/> <strong>{e}</strong>'

          messages.add_message(request, messages.INFO, msj)
          '''
          return JsonResponse({
               'nombre': nombre,
               'apellido': apellido,
               'correo': correo,
               'twitter': twitter,
               'Ok': True,
               'msj' : 'El participante ha sido registrado con exito'
          })
          '''

          #ctx = {
           
          #    'participantes':  Participantes.objects.all().order_by('nombre')
          #}
          
          #return HttpResponse('El participante ha sido registrado')
          #return render(request, 'registro/participantes.html', ctx)
     
     #Metodo GET, PUT, PATVH, DELETE

     #la primera consulta: select * from participantes
     #realizar un Queryset con el ORM de DJANGO

     activo = 'participantes'
     q = request.GET.get('q')

     if q:
          data = Participantes.objects.filter(nombre__startswith = q).order_by('nombre')
          '''
               select * from participantes
               where nombre like 'n%'
          '''
     else:
          data = Participantes.objects.all().order_by('nombre')


     

     ctx = {
          'activo': activo,
          'participantes': data,
          'q' : q,
     }
          
     return render(request, 'registro/participantes.html', ctx)


@login_required
def eliminar_participantes(request, id):


     Participantes.objects.get(pk=id).delete()

     return redirect(reverse('participantes'))


@login_required
def editar_participantes(request, id):
     par = get_object_or_404(Participantes, pk=id)

     if request.method ==  'POST':
          nombre = request.POST.get('nombre')
          apellido = request.POST.get('apellido')
          correo = request.POST.get('correo')
          twitter = request.POST.get('twitter')

          par.nombre = nombre
          par.apellido = apellido
          par.correo = correo
          par.twitter = twitter
          par.save()



     #par = Participantes.objects.get(pk=id)
     data = Participantes.objects.all().order_by('nombre')
     
     ctx = {
          'activo': participantes,
          'participantes': data,
          'p': par,
     }
          
     return render(request, 'registro/participantes.html', ctx)


@login_required
def conferencias(request):
     confs = Conferencia.objects.filter(estado = '1').order_by('fecha')

     return render(request, 'registro/conferencias.html', {'confs' : confs})