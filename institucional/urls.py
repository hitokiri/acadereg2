from django.conf.urls import url,patterns

urlpatterns = patterns('institucional.views',
	url(r'^$','vista_index',name = 'inicio'),
	# url(r'^login$','inicia_secion',name = 'inicio_de_secion' ),
	url(r'^maestro/add$', 'maestros_view', name='agregarmaestros' ),
	)