# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'PostMark'
        db.create_table('reader_postmark', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('posting', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reader.Posting'])),
            ('mark', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('reader', ['PostMark'])

        # Adding model 'Category'
        db.create_table('reader_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('parentcat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reader.Category'], null=True, blank=True)),
        ))
        db.send_create_signal('reader', ['Category'])

        # Adding field 'Feed.category'
        db.add_column('reader_feed', 'category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reader.Category'], null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'PostMark'
        db.delete_table('reader_postmark')

        # Deleting model 'Category'
        db.delete_table('reader_category')

        # Deleting field 'Feed.category'
        db.delete_column('reader_feed', 'category_id')


    models = {
        'reader.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parentcat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reader.Category']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'publishdate': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 28, 22, 2, 5, 402813)'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'reader.postmark': {
            'Meta': {'object_name': 'PostMark'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mark': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'posting': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reader.Posting']"})
        }
    }

    complete_apps = ['reader']
