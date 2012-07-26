# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Posting'
        db.create_table('reader_posting', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('publishdate', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 7, 26, 22, 40, 42, 988405))),
            ('feed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reader.Feed'])),
        ))
        db.send_create_signal('reader', ['Posting'])

        # Adding model 'Feed'
        db.create_table('reader_feed', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('reader', ['Feed'])


    def backwards(self, orm):
        
        # Deleting model 'Posting'
        db.delete_table('reader_posting')

        # Deleting model 'Feed'
        db.delete_table('reader_feed')


    models = {
        'reader.feed': {
            'Meta': {'object_name': 'Feed'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'reader.posting': {
            'Meta': {'object_name': 'Posting'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reader.Feed']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publishdate': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 26, 22, 40, 42, 988405)'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['reader']
