# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Documentos'
        db.create_table('alumnos_documentos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo_alumno', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['alumnos.Alumnos'], unique=True)),
            ('partida_nacimiento', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('Fotografia', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('certificado', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('constancia_conducta', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('constancia_medica', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('alumnos', ['Documentos'])

        # Adding model 'Alumnos'
        db.create_table('alumnos_alumnos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo_alumno', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nombres', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('edad', self.gf('django.db.models.fields.IntegerField')()),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('fnacimiento', self.gf('django.db.models.fields.DateField')()),
            ('telefono', self.gf('django.db.models.fields.IntegerField')(max_length=8)),
            ('padre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('madre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('encargado', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('parentesco', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('direccion', self.gf('django.db.models.fields.TextField')(max_length=100)),
            ('estado', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('grado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['institucional.Grados'])),
            ('documentacion', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('alumnos', ['Alumnos'])


    def backwards(self, orm):
        # Deleting model 'Documentos'
        db.delete_table('alumnos_documentos')

        # Deleting model 'Alumnos'
        db.delete_table('alumnos_alumnos')


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
        'alumnos.documentos': {
            'Fotografia': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'Meta': {'ordering': "('codigo_alumno',)", 'object_name': 'Documentos'},
            'certificado': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'codigo_alumno': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['alumnos.Alumnos']", 'unique': 'True'}),
            'constancia_conducta': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'constancia_medica': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partida_nacimiento': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
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
        }
    }

    complete_apps = ['alumnos']