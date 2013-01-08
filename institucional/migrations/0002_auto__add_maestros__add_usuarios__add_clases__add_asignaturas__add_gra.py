# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Maestros'
        db.create_table('institucional_maestros', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombres', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('edad', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('aingreso', self.gf('django.db.models.fields.DateField')()),
            ('estudio', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('telefono', self.gf('django.db.models.fields.IntegerField')(max_length=8)),
            ('direccion', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('estado', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('institucional', ['Maestros'])

        # Adding model 'Usuarios'
        db.create_table('institucional_usuarios', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('rol', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['institucional.Roles'])),
        ))
        db.send_create_signal('institucional', ['Usuarios'])

        # Adding model 'Clases'
        db.create_table('institucional_clases', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('grado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['institucional.Grados'])),
            ('maestro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['institucional.Maestros'])),
            ('alumno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alumnos.Alumnos'])),
            ('materia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['institucional.Asignaturas'])),
            ('hora', self.gf('django.db.models.fields.TimeField')()),
            ('dia', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('institucional', ['Clases'])

        # Adding model 'Asignaturas'
        db.create_table('institucional_asignaturas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('asignatura', self.gf('django.db.models.fields.CharField')(max_length=17)),
            ('grado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['institucional.Grados'])),
            ('maeestro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['institucional.Maestros'])),
            ('estado', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('basic', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('institucional', ['Asignaturas'])

        # Adding model 'Grados'
        db.create_table('institucional_grados', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('maestro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['institucional.Maestros'])),
            ('nivel', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('grado', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('estado', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('institucional', ['Grados'])

        # Adding model 'Roles'
        db.create_table('institucional_roles', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('institucional', ['Roles'])


    def backwards(self, orm):
        # Deleting model 'Maestros'
        db.delete_table('institucional_maestros')

        # Deleting model 'Usuarios'
        db.delete_table('institucional_usuarios')

        # Deleting model 'Clases'
        db.delete_table('institucional_clases')

        # Deleting model 'Asignaturas'
        db.delete_table('institucional_asignaturas')

        # Deleting model 'Grados'
        db.delete_table('institucional_grados')

        # Deleting model 'Roles'
        db.delete_table('institucional_roles')


    models = {
        'alumnos.alumnos': {
            'Meta': {'ordering': "('grado',)", 'object_name': 'Alumnos'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'codigo_alumno': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'direccion': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'documentacion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'encargado': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'estado': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fnacimiento': ('django.db.models.fields.DateField', [], {}),
            'grado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['institucional.Grados']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'madre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'padre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parentesco': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {'max_length': '8'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'institucional.asignaturas': {
            'Meta': {'object_name': 'Asignaturas'},
            'asignatura': ('django.db.models.fields.CharField', [], {'max_length': '17'}),
            'basic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estado': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'grado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['institucional.Grados']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maeestro': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['institucional.Maestros']"})
        },
        'institucional.clases': {
            'Meta': {'object_name': 'Clases'},
            'alumno': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['alumnos.Alumnos']"}),
            'dia': ('django.db.models.fields.DateField', [], {}),
            'grado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['institucional.Grados']"}),
            'hora': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maestro': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['institucional.Maestros']"}),
            'materia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['institucional.Asignaturas']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'institucional.grados': {
            'Meta': {'object_name': 'Grados'},
            'estado': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'grado': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maestro': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['institucional.Maestros']"}),
            'nivel': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'institucional.maestros': {
            'Meta': {'object_name': 'Maestros'},
            'aingreso': ('django.db.models.fields.DateField', [], {}),
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'direccion': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'edad': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'estado': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'estudio': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {'max_length': '8'})
        },
        'institucional.roles': {
            'Meta': {'object_name': 'Roles'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'institucional.usuarios': {
            'Meta': {'object_name': 'Usuarios'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rol': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['institucional.Roles']"}),
            'usuario': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['institucional']