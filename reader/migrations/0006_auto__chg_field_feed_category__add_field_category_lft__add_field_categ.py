# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Feed.category'
        db.alter_column('reader_feed', 'category_id', self.gf('mptt.fields.TreeForeignKey')(null=True, to=orm['reader.Category']))

        # Adding field 'Category.lft'
        db.add_column('reader_category', 'lft', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True), keep_default=False)

        # Adding field 'Category.rght'
        db.add_column('reader_category', 'rght', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True), keep_default=False)

        # Adding field 'Category.tree_id'
        db.add_column('reader_category', 'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True), keep_default=False)

        # Adding field 'Category.level'
        db.add_column('reader_category', 'level', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True), keep_default=False)

        # Changing field 'Category.parent'
        db.alter_column('reader_category', 'parent_id', self.gf('mptt.fields.TreeForeignKey')(null=True, to=orm['reader.Category']))


    def backwards(self, orm):
        
        # Changing field 'Feed.category'
        db.alter_column('reader_feed', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reader.Category'], null=True))

        # Deleting field 'Category.lft'
        db.delete_column('reader_category', 'lft')

        # Deleting field 'Category.rght'
        db.delete_column('reader_category', 'rght')

        # Deleting field 'Category.tree_id'
        db.delete_column('reader_category', 'tree_id')

        # Deleting field 'Category.level'
        db.delete_column('reader_category', 'level')

        # Changing field 'Category.parent'
        db.alter_column('reader_category', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['reader.Category']))


    models = {
        'reader.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'subcategories'", 'null': 'True', 'to': "orm['reader.Category']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
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
            'category': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'feeds'", 'null': 'True', 'to': "orm['reader.Category']"}),
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
            'publishdate': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 3, 22, 27, 32, 461043)'}),
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
