from django.shortcuts import render
from django.http import HttpResponse


participantes = [
     {
          'nombre': 'Juan',
          'apellido': 'Lopez',
          'correo' : 'jaun@gmail.com',
          'twitter': 'juan.lopez'
     },
     {
          'nombre': 'Maria',
          'apellido': 'Gomez',
          'correo' : 'maria@gmail.com',
          'twitter': 'maria.gomez'
     },
     {
          'nombre': 'Karla',
          'apellido': 'Herrera',
          'correo' : 'karla.herrera@gmail.com',
          'twitter': 'karla.herrerra'
     },
     {
          'nombre': 'Josue',
          'apellido': 'Alvarez',
          'correo' : 'JosueAlvarez@gmail.com',
          'twitter': 'Josuetec2003'
     }
]
# Create your views here.
def tarea(request): 

     

     if request.method == 'POST':
          nombre = request.POST.get('nombre')
          apellido = request.POST.get('apellido')
          correo = request.POST.get('correo')
          twitter = request.POST.get('twitter')

          participantes.append({
               'nombre': nombre,
               'apellido': apellido,
               'correo' : correo,
               'twitter': twitter,
          })

          ctx = {
               'participantes': participantes
          }
          
          #return HttpResponse('El participante ha sido registrado')
          return render(request, 'Tarea1/index.html', ctx)
     else:
          #el metodo GET
          #contexto q va pa la plantilla
          ctx = {
               'participantes': participantes
          }
          
          return render(request, 'Tarea1/index.html', ctx)