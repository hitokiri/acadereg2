# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from institucional.forms import  MaestrosForms
from institucional.models  import Maestros
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
def vista_index(request):
	titulo = 'Nombre Colegio'
	logo = 'Aqui el logo'
	ctx = {'titulo' : titulo, 'logo' : logo}
	return render_to_response('index.html',ctx,context_instance=RequestContext(request))

# def inicia_secion(request):
# 	if request.method == 'POST':
# 		formulario = Secion(request.POST)
# 		if formulario.is_valid():
# 			nombre = formulario.cleaned_data['usuario']
# 			password = make_password(formulario.cleaned_data['password'])
# 			p = Usuarios()
# 			p.usuario = nombre
# 			p.password = password
# 			p.save()
# 			return HttpResponseRedirect('/login')
# 	else:
# 		saber = Usuarios.objects.get(usuario = 'mercurio')
# 		correcto = check_password('kanguro',saber.password)
# 		formulario = Secion()
# 	ctx = {'Titulo':'Inicio de Seción'}
# 	return render_to_response('inicio_secion.html',ctx,context_instance=RequestContext(request))


def maestros_view(request):
	datos = Maestros.objects.all()
	if request.method == 'POST':
		formulario = MaestrosForms(request.POST)
		if formulario.is_valid():
			formulario.save();
			return HttpResponseRedirect('/login')
	else:
		formulario =MaestrosForms()
	ctx ={'formulario':formulario,'datos':datos}
	return render_to_response('maestros.html',ctx,context_instance = RequestContext(request))