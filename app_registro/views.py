from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): 
   
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
       },{
            'nombre': 'Josue',
            'apellido': 'Alvarez',
            'correo' : 'JosueAlvarez@gmail.com',
            'twitter': 'Josuetec2003'
       }
   ]
    #contexto q va pa la plantilla
   ctx = {
       'participantes': participantes
   }

   return render(request, 'registro/index.html', ctx)