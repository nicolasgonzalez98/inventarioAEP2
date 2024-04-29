from django.db import models
from django.contrib.auth import get_user_model
from django.forms import model_to_dict
from django.contrib.auth.models import Group
from django.utils import timezone


# Create your models here.

##Opciones



User = get_user_model()

class Tecnico(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    id_user = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre+ ' ' + self.apellido

class Tipo(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self) -> str:
        return self.name

class Marca(models.Model):
    nombre = models.CharField(max_length=50, null=False, default='S/D', unique=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    nombre = models.CharField(max_length=100, null=False, default='S/D')

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    
    

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    estados_hardware = (
    ("Nuevo", "Nuevo"),
    ('Activo', 'Activo'),
    ('En uso', 'En uso'),
    ('Fuera de Servicio', 'Fuera de Servicio'),
    ('Scrap', 'Scrap'),
    ('RMA', 'RMA')
)
    nombre = models.CharField(choices=estados_hardware, max_length=50)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre}'

class Hardware(models.Model):
    origenes = (
        ('T4', 'T4'),
        ('CAU', 'CAU'),
        ('Yenny', 'Yenny')
    )

    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    nro_de_serie = models.CharField(max_length=100, blank=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    observaciones = models.TextField(max_length=500, blank=True)
    origen = models.CharField(choices=origenes, max_length=10, default='CAU')
    nota = models.TextField(max_length=500, blank=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item
    

    def __str__(self):
        return f'{self.tipo}'
    
    class Meta:
        ordering = ['tipo']

class Contador(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    cantidad = models.IntegerField(default=0)

    def toJSON(self):
        item = model_to_dict(self)
        return item

class Notificacion(models.Model):
    hardware = models.ForeignKey(Hardware, on_delete=models.CASCADE, db_constraint=False)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    realizado = models.BooleanField(default=False)
    tipo = models.CharField(max_length=20)
    estado = models.CharField(max_length=50)
    nro_de_serie = models.CharField(max_length=100)

    def toJSON(self):
        item = model_to_dict(self)
        return item

class Asignacion(models.Model):
    hardware = models.ForeignKey(Hardware, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=50)
    fecha_creacion = models.DateField(default=timezone.now)
    nro_ticket = models.CharField(blank=True, max_length=10)
    nota = models.TextField(blank=True, max_length=200)

    def toJSON(self):
        item = model_to_dict(self)
        return item
    
    class Meta:
        ordering = ['fecha_creacion']

    def __str__(self):
        return f'{self.usuario} - {self.fecha_creacion}'
    
    