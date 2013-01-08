#encoding:utf-8
from django.forms import ModelForm, Textarea,TextInput
from django import forms
from alumnos.models import Alumnos , Documentos


class AlumnoForm(ModelForm):
	class  Meta:
		model 		= Alumnos

class DocumentosForm(ModelForm):
	class  Meta:
		model 		= Documentos