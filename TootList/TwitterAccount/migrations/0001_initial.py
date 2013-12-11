# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TwitterAccount'
        db.create_table(u'TwitterAccount_twitteraccount', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.TextField')()),
            ('twitter_consumer_key', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('twitter_consumer_secret', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('twitter_access_token', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('twitter_access_token_secret', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tweet_frequency', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'TwitterAccount', ['TwitterAccount'])

        # Adding M2M table for field times_to_run on 'TwitterAccount'
        m2m_table_name = db.shorten_name(u'TwitterAccount_twitteraccount_times_to_run')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('twitteraccount', models.ForeignKey(orm[u'TwitterAccount.twitteraccount'], null=False)),
            ('timetorun', models.ForeignKey(orm[u'TwitterAccount.timetorun'], null=False))
        ))
        db.create_unique(m2m_table_name, ['twitteraccount_id', 'timetorun_id'])

        # Adding model 'TimeToRun'
        db.create_table(u'TwitterAccount_timetorun', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_string', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'TwitterAccount', ['TimeToRun'])


    def backwards(self, orm):
        # Deleting model 'TwitterAccount'
        db.delete_table(u'TwitterAccount_twitteraccount')

        # Removing M2M table for field times_to_run on 'TwitterAccount'
        db.delete_table(db.shorten_name(u'TwitterAccount_twitteraccount_times_to_run'))

        # Deleting model 'TimeToRun'
        db.delete_table(u'TwitterAccount_timetorun')


    models = {
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
            'username': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['TwitterAccount']