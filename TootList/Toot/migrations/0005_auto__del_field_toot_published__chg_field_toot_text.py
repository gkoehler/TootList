# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Toot.published'
        db.delete_column(u'Toot_toot', 'published')


        # Changing field 'Toot.text'
        db.alter_column(u'Toot_toot', 'text', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Adding field 'Toot.published'
        db.add_column(u'Toot_toot', 'published',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Toot.text'
        db.alter_column(u'Toot_toot', 'text', self.gf('django.db.models.fields.TextField')(max_length=140))

    models = {
        u'Toot.toot': {
            'Meta': {'ordering': "['pub_date']", 'object_name': 'Toot'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['TwitterAccount.TwitterAccount']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 12, 11, 0, 0)'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'TwitterAccount.timetorun': {
            'Meta': {'object_name': 'TimeToRun'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_string': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'TwitterAccount.twitteraccount': {
            'Meta': {'object_name': 'TwitterAccount'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'times_to_run': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['TwitterAccount.TimeToRun']", 'symmetrical': 'False'}),
            'tweet_frequency': ('django.db.models.fields.IntegerField', [], {}),
            'twitter_access_token': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'twitter_access_token_secret': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'twitter_consumer_key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'twitter_consumer_secret': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['Toot']