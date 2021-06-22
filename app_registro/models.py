from django.db import models
from django.db.models.fields import DateTimeField
from datetime import datetime, timedelta
'''
    Tipos de datos para los campos de los modelos:
    - Todos los campos se obtienen de models
    -> CharField(max_lenght=25, default='Jack', null=True, blank=True)
    -> TextField()
    -> IntegerField()
    -> DecimalField(max_digits=5, decimal_places=2)
    -> PositiveIntegerField()
    -> SmallIntegerField()
    -> BooleanField(default=True)
    -> EmailField()
    -> ImageField(upload_to='fotos')
    -> FileField(upload_to='archivos')
    -> SlugField(): Tesla ha afectado el precio del Bitcoin >> tesla-ha-afectado-....
    Campos para establecer relaciones entre Modelos:
    -> ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    -> OneToOneField()
    -> ManyToManyField()
'''
# Create your models here.
class Conferencista(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    experiencia = models.TextField(null=True)
    foto = models.ImageField(upload_to = 'conferencistas', null = True, blank = True)

    def __str__(self) -> str:
        return self.nombre



class Conferencia(models.Model):
    ESTADOS = (
        ('1', 'Pendiente'),
        ('2', 'En Proceso'),
        ('3', 'Finalizada'),
        ('4', 'Cancelada'),
    )
    nombre = models.CharField('Nombre Completo', max_length=35)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha = models.DateField()
    hora = models.TimeField()
    duracion = models.SmallIntegerField(default='2')
    conferencista = models.ManyToManyField(Conferencista, blank=True)
    estado = models.CharField(max_length=1, choices=ESTADOS, default='1')
    cupos = models.SmallIntegerField(default=10)

    @property
    def tiempo_restante(self):
        hoy = datetime.now().date()

        if hoy > self.fecha: #la conferencia ya paso
            dias = (hoy - self.fecha).days
            return f'La conferencia ya pasó, hace {dias}'
        elif hoy == self.fecha:
            return 'La conferencia es hoy'
        else:
            dias = (self.fecha - hoy).days
            return f'La conferencia es dentro de {dias} dias'

    def __str__(self):
        return f'Conferencia: {self.nombre}'

class Participantes(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    correo = models.EmailField()
    twitter = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'


class Asistencia(models.Model):
    conferencia = models.ForeignKey(Conferencia, on_delete=models.CASCADE)
    participante = models.ForeignKey(Participantes, on_delete=models.CASCADE)
    confirmacion = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.conferencia} - {self.participante}'

    class Meta: 
        unique_together = ('conferencia', 'participante')


