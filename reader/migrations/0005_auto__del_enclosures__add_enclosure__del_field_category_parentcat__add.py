# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Enclosures'
        db.delete_table('reader_enclosures')

        # Adding model 'Enclosure'
        db.create_table('reader_enclosure', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('posting', self.gf('django.db.models.fields.related.ForeignKey')(related_name='enclosures', to=orm['reader.Posting'])),
            ('etype', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('length', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('href', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('reader', ['Enclosure'])

        # Deleting field 'Category.parentcat'
        db.delete_column('reader_category', 'parentcat_id')

        # Adding field 'Category.parent'
        db.add_column('reader_category', 'parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='category', null=True, to=orm['reader.Category']), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'Enclosures'
        db.create_table('reader_enclosures', (
            ('posting', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reader.Posting'])),
            ('href', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('length', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('etype', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('reader', ['Enclosures'])

        # Deleting model 'Enclosure'
        db.delete_table('reader_enclosure')

        # Adding field 'Category.parentcat'
        db.add_column('reader_category', 'parentcat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reader.Category'], null=True, blank=True), keep_default=False)

        # Deleting field 'Category.parent'
        db.delete_column('reader_category', 'parent_id')


    models = {
        'reader.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'category'", 'null': 'True', 'to': "orm['reader.Category']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'reader.enclosure': {
            'Meta': {'object_name': 'Enclosure'},
            'etype': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'posting': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'enclosures'", 'to': "orm['reader.Posting']"})
        },
        'reader.feed': {
            'Meta': {'object_name': 'Feed'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reader.Category']", 'null': 'True', 'blank': 'True'}),
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
            'origid': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'publishdate': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 28, 22, 6, 14, 740007)'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'reader.postmark': {
            'Meta': {'object_name': 'PostMark'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mark': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'posting': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'marks'", 'to': "orm['reader.Posting']"})
        }
    }

    complete_apps = ['reader']
