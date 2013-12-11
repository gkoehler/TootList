# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Toot'
        db.create_table(u'Toot_toot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('published', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'Toot', ['Toot'])


    def backwards(self, orm):
        # Deleting model 'Toot'
        db.delete_table(u'Toot_toot')


    models = {
        u'Toot.toot': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Toot'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'published': ('django.db.models.fields.BooleanField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['Toot']