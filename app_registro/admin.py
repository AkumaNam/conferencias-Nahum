from django.contrib import admin
from django.contrib.admin.decorators import register
from app_registro.models import Conferencia, Conferencista, Participantes
# Register your models here.
class ConferenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha', 'hora', 'conferencista')
    list_editable = ('nombre', 'conferencista')




admin.site.register(Conferencia, ConferenciaAdmin)




admin.site.register(Conferencista)



admin.site.register(Participantes)