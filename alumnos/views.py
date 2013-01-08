from django.shortcuts import render_to_response
from django.template import RequestContext
from alumnos.forms import AlumnoForm
from alumnos.models import Documentos , Alumnos
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password

# def vista_inscripcion(request):
# 	consulta = Alumnos.objects.all()
# 	formulario = AlumnoForm(instance = request.user)
# 	ctx ={'formulario': formulario}
# 	return render_to_response ('inscripcion.html',ctx,context_instance=RequestContext(request))
def create_password(request):

	hola = make_password('amaron',)
	ctx = {'hola':hola}
	return render_to_response('ver.html',ctx,)
#formulario para la inscripcion de nuevos alumnos
def vista_inscripcion(request):

	vista = 'Inscripcion de alumnos' #el nombre de la pagina en la que nos encontramos
	if request.method == 'POST':
		formulario =AlumnoForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/alumnos/inscripcion')
	else:
		formulario = AlumnoForm()
	ctx ={'formulario': formulario , 'pagina':vista}
	return render_to_response ('alumnos/inscripcion.html',ctx,context_instance=RequestContext(request))

def datos_usuarios(request):
	datos = Alumnos.objects.get(pk = 0)
	fotos = Documentos.objects.get(pk = datos.codigo_alumno)
	ctx = {'fotos':fotos, 'datos':datos}
	return render_to_response('alumnos/detallesalumnos.html',ctx,context_instance=RequestContext(request) )

