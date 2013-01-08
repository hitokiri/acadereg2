from alumnos.models import Alumnos , Documentos
from django.contrib import admin

class AcaderegAlumnosAdmin(admin.TabularInline):
	model = Documentos
	extra = 1

class AlumnosAdmin(admin.ModelAdmin):
		inlines = [AcaderegAlumnosAdmin]

admin.site.register(Alumnos , AlumnosAdmin)

