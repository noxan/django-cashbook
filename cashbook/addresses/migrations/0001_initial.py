# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table('addresses_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('addresses', ['Country'])

        # Adding model 'State'
        db.create_table('addresses_state', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addresses.Country'])),
        ))
        db.send_create_signal('addresses', ['State'])

        # Adding model 'City'
        db.create_table('addresses_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('zipcode', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addresses.State'])),
        ))
        db.send_create_signal('addresses', ['City'])

        # Adding model 'Street'
        db.create_table('addresses_street', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addresses.City'])),
        ))
        db.send_create_signal('addresses', ['Street'])

        # Adding model 'Address'
        db.create_table('addresses_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('street', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addresses.Street'])),
            ('street_number', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('addresses', ['Address'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table('addresses_country')

        # Deleting model 'State'
        db.delete_table('addresses_state')

        # Deleting model 'City'
        db.delete_table('addresses_city')

        # Deleting model 'Street'
        db.delete_table('addresses_street')

        # Deleting model 'Address'
        db.delete_table('addresses_address')


    models = {
        'addresses.address': {
            'Meta': {'object_name': 'Address'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'street': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['addresses.Street']"}),
            'street_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'addresses.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['addresses.State']"}),
            'zipcode': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'addresses.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'addresses.state': {
            'Meta': {'object_name': 'State'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['addresses.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'addresses.street': {
            'Meta': {'object_name': 'Street'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['addresses.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['addresses']