from django.db import models


class Alumnos(models.Model):
	escojer_edad =((1, 1),(2, 2),(3, 3),(4, 4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),
		(11,11),(12,12),(13,13),(14,14),(15,15),(16,16),(17,17),(18,18),(19,19),(20,20),)
	sexo 						= (('F','Femenino'),('M','Masculino'),)
	Parentesco 					= (('P','Padre'),('F','Familiar'),)
	codigo_alumno				= models.CharField("codigo del Alumno", max_length = 10)
	nombres 					= models.CharField(max_length = 100)
	apellidos 					= models.CharField(max_length = 100)
	edad 						= models.IntegerField(choices = escojer_edad)
	sexo 						= models.CharField(max_length = 1, choices = sexo)
	fnacimiento 				= models.DateField("fecha de nacimiento ")
	telefono 					= models.IntegerField(max_length = 8)
	padre 						= models.CharField("Nombre de el Padre", max_length = 100)
	madre 						= models.CharField("Nombre de la Madre", max_length = 100)
	encargado 					= models.CharField(max_length = 100)
	parentesco 					= models.CharField(max_length = 1 ,choices = Parentesco)
	direccion 					= models.TextField(max_length = 100)
	estado 						= models.BooleanField(default = True)
	grado						= models.ForeignKey('institucional.Grados')
	documentacion 				= models.BooleanField()

	def __unicode__(self):
		return '%s . %s' %(self.nombres.title() , self.apellidos[0:2].title())
	#crear la reversa o modificacion de el campo
	class Meta:
		ordering = ('grado',)

#modelo de la documentacion
class Documentos(models.Model):
	#este campo solo sirve para hacer referencia no aparecera en el formulario
	codigo_alumno 				= models.OneToOneField('Alumnos')
	partida_nacimiento 			= models.FileField(upload_to = "partidas", \
												   verbose_name = u'partidas')
	Fotografia 					= models.ImageField(upload_to = "alumnos",verbose_name = u'foto alumno')
	certificado		 			= models.FileField(upload_to = "certificados", verbose_name = u'certificados' )
	constancia_conducta			= models.FileField(upload_to = "conducta", verbose_name = u'constacia de conducta')
	constancia_medica 			= models.FileField(upload_to = "medica", verbose_name = u'constancia medica' )

	def __unicode__(self):
		return self.codigo_alumno

	class Meta:
		ordering = ('codigo_alumno',)