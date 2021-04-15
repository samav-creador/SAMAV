from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

#tabla especialidad
class Especialidad(models.Model):
	nombre_esp = models.CharField(max_length = 100, verbose_name = 'Nombre_Especialidad')
	class Meta:
		verbose_name = 'Especialidad'
		verbose_name_plural = 'Especialidades'
	def __str__(self):
		return str(self.nombre_esp)

#tabla materia
class Materia(models.Model):
	nombre = models.CharField(max_length = 200, null=True, blank=True)
	grupo = models.CharField(max_length = 50, verbose_name = 'Grupo', null=True, blank=True)

	class Meta:
		verbose_name = 'Materia'
		verbose_name_plural = 'Materias'
	def __str__(self):
		return str(self.nombre)

#tabla grupo
class Grupo(models.Model):
	nombre = models.CharField(max_length = 30)
	especialidad = models.CharField(max_length = 50, verbose_name = 'Especialidad')

	class meta:
		verbose_name = 'Grupo'
		verbose_name_plural = 'Grupos'
	def __str__(self):
		return str(self.nombre)

#tabla alumno
class Alumno(models.Model):
	matricula = models.CharField(max_length=20, null=True, blank=True)
	nombre = models.CharField(max_length = 150, verbose_name = 'Nombre completo')
	grupo = models.CharField(max_length = 30, verbose_name = 'Grupo')
	class Meta:
		verbose_name = 'Alumno'
		verbose_name_plural = 'Alumnos'
	def __str__(self):
		return str(self.nombre)

#tabla tipo incidencia
class tipoIncidencia(models.Model):
	nombre = models.CharField(max_length = 100)
	class Meta:
		verbose_name = 'tipoIncidencia'
		verbose_name_plural = 'tipoIncidencias'
	def __str__(self):
		return str(self.nombre)

#tabla problemática
class Problematica(models.Model):
	tipo = models.ForeignKey(tipoIncidencia, on_delete = models.CASCADE)
	descripcion = models.CharField(max_length = 120)
	solucion = models.CharField(max_length = 120)
	grupo = models.ForeignKey(Grupo, on_delete = models.CASCADE)
	alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE)
	user = models.ForeignKey(User, default='', on_delete = models.CASCADE)
	materia = models.ForeignKey(Materia, on_delete = models.CASCADE)
	parcial = models.IntegerField(verbose_name = 'Parcial', null=True, blank=True)
	semana = models.IntegerField(verbose_name = 'Semana', null=True, blank=True)
	fecha = models.DateField(null=True,blank=True,verbose_name = 'Fecha',default= now )
	class Meta:
		verbose_name = 'Problematica'
		verbose_name_plural = 'Problematicas'

	def __str__(self):
		return 'Incidencia %s del alumn@ %s' % (self.tipo, self.alumno)

class Macros(models.Model):
	url = models.CharField(max_length = 255)

	def __str__(self):
		return str(self.url)