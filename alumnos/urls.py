from django.conf.urls import url, patterns

urlpatterns = patterns('alumnos.views',
	url(r'^alumnos/inscripcion$','vista_inscripcion', name = 'alumno_inscripcion'),
	url(r'^password$','create_password', name = 'password'),
	)