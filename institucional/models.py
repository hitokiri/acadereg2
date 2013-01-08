# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


sexo 							= (('F','Femenino'),('M','Masculino'),)
# Create your models here.
class Grados(models.Model):
	maestro 					= models.ForeignKey('Maestros')
	nivel						= models.CharField(max_length = 10)
	grado 						= models.CharField(max_length = 50)
	estado 						= models.BooleanField(default=True)
	def __unicode__(self):
		return self.grado

class Maestros(models.Model):
	nombres 					= models.CharField(max_length = 100)
	apellidos 					= models.CharField(max_length = 100)
	edad 						= models.IntegerField(max_length = 2)
	sexo 						= models.CharField(max_length = 1, choices = sexo)
	aingreso 					= models.DateField()
	estudio 					= models.CharField(max_length = 75)
	telefono 					= models.IntegerField(max_length = 8)
	direccion 					= models.TextField(max_length = 200)
	estado 						= models.BooleanField(default = True)
	def __unicode__(self):
		return self.nombres

class Asignaturas(models.Model):
	asignatura 					= models.CharField(max_length = 17)
	grado						= models.ForeignKey('Grados')
	maeestro 					= models.ForeignKey('Maestros')
	estado 						= models.BooleanField(default = True)
	basic 						= models.BooleanField(default = False)
	def __unicode__(self):
		return self.asignatura

class Usuarios(models.Model):
	usuario 					= models.OneToOneField(User)
	rol 						= models.ForeignKey('Roles')

class Roles(models.Model):
	codigo						= models.CharField(max_length = 12)
	nombre 						= models.CharField(max_length = 20)

class Clases(models.Model):
	nombre 						= models.CharField(max_length = 20)
	grado 						= models.ForeignKey("Grados")
	maestro 					= models.ForeignKey("Maestros")
	alumno 						= models.ForeignKey("alumnos.Alumnos")
	materia 					= models.ForeignKey("Asignaturas")
	hora 						= models.TimeField()
	dia 						= models.DateField()