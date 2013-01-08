from django.forms import ModelForm, Textarea,TextInput, PasswordInput

from institucional.models import Usuarios, Maestros

# class Secion(ModelForm):
# 	class Meta:
# 		model 		= Usuarios
# 		fields 		=('usuario','password',)
# 		widgets 	= {'usuario': TextInput, 'password':PasswordInput()}

class MaestrosForms(ModelForm):
	class Meta:
		model = Maestros
