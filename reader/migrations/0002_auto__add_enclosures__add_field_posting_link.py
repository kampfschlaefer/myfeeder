# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Enclosures'
        db.create_table('reader_enclosures', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('posting', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reader.Posting'])),
            ('etype', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('length', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('href', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('reader', ['Enclosures'])

        # Adding field 'Posting.link'
        db.add_column('reader_posting', 'link', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Enclosures'
        db.delete_table('reader_enclosures')

        # Deleting field 'Posting.link'
        db.delete_column('reader_posting', 'link')


    models = {
        'reader.enclosures': {
            'Meta': {'object_name': 'Enclosures'},
            'etype': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'posting': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reader.Posting']"})
        },
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
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'publishdate': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 26, 22, 56, 36, 701049)'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['reader']
