# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Toot.account'
        db.add_column(u'Toot_toot', 'account',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['TwitterAccount.TwitterAccount']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Toot.account'
        db.delete_column(u'Toot_toot', 'account_id')


    models = {
        u'Toot.toot': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Toot'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['TwitterAccount.TwitterAccount']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'published': ('django.db.models.fields.BooleanField', [], {}),
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