
from app_registro.models import Participantes
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib import messages



# Create your views here.
def index(request):
     return render(request, 'registro/index.html')


def participantes(request): 

     

     if request.method == 'POST':
          nombre = request.POST.get('nombre')
          apellido = request.POST.get('apellido')
          correo = request.POST.get('correo')
          twitter = request.POST.get('twitter')

          p = Participantes(nombre = nombre, apellido = apellido, correo = correo, twitter = twitter)
          p.save()
          
          messages.add_message(request, messages.INFO, 'El participante {nombre} {apellido} ha sido registrado con exito')
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
     data = Participantes.objects.all().order_by('nombre')

     ctx = {
          'participantes': data
     }
          
     return render(request, 'registro/participantes.html', ctx)
