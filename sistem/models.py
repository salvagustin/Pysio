from django.db import models
import datetime

horayfecha = datetime.datetime.now()
semanaactual = horayfecha.isocalendar().week

# Create your models here.
class Paciente(models.Model):
    idpaciente = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=300)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', null = False)
    telefono = models.PositiveIntegerField('Telefono')
    Opciones = (("M", "Masculino"), ("F", "Femenino"))
    sexo =  models.CharField('Sexo', max_length=1, choices=Opciones, blank=False, null=False)

    def __str__(self):
        return f"{self.nombre}"


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=False, null=True)
    user = models.CharField('Usuario', max_length=100,unique=True)
    token = models.PositiveIntegerField('Token',unique=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=True, auto_now_add=False)
    opciones = (("Admin", "Administrador"), ("Clien", "Cliente"))
    tipousuario =  models.CharField('Tipo de usuario', max_length=5, choices=opciones, blank=True, null=True)
    
    def __str__(self):
        return f"{self.paciente.nombre} - {self.token}"


class Consulta(models.Model):
    idconsulta = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=False, null=False)
    fechaconsulta = models.DateField('Fecha de consulta', auto_now=True, auto_now_add=False)
    horaconsulta = models.TimeField('Hora consulta', auto_now=True, auto_now_add=False)
    precioconsulta = models.DecimalField('Precio', max_digits=10, decimal_places=2, default=0.0, blank=False, null=False)
    opciones = (("Lesion", "Lesion"), ("Patologia", "Patologia"))
    tipo =  models.CharField('Tipo', max_length=9, choices=opciones, blank=False, null=False)
    observaciones = models.CharField('Observaciones', max_length=500)
   
    
    def __str__(self):
        return f"{self.idconsulta} {self.paciente.nombre}"
    
#class Ejercicio(models.Model):
 #   idejercicio = models.AutoField(primary_key=True)
 #categoria
 #subcategoria
  #  nombre = models.CharField('Nombre', max_length=300)
   # semana = models.PositiveIntegerField('Semana')
    #descripcion = models.CharField('Descripcion', max_length=300)
    # Imagen
    # Video
    # lesion o patologia
    # subir pdf


class Cita(models.Model):
    idcita = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=False, null=False)
    fechacita = models.DateField('Fecha de cita')
    opciones = (("1", "8:00 - 9:00"), ("2", "9:00 - 10:00"),("3", "10:00 - 11:00"),("4", "11:00 - 12:00"),
                ("5", "01:00 - 02:00"),("6", "02:00 - 03:00"),("7", "03:00 - 04:00"),("8", "04:00 - 05:00"),("9", "05:00 - 06:00"))
    horacita =  models.CharField('Hora cita', max_length=11, choices=opciones, blank=False, null=False)
    observaciones = models.CharField('Observaciones', max_length=500)