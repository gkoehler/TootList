from django.db import models
import time

# Create your models here.
class TwitterAccount(models.Model):
	username = models.CharField(max_length=20)

	twitter_consumer_key = models.CharField(max_length=255)
	twitter_consumer_secret = models.CharField(max_length=255)
	twitter_access_token = models.CharField(max_length=255)
	twitter_access_token_secret = models.CharField(max_length=255)

	tweet_frequency = models.IntegerField('Tweets per day')

	times_to_run = models.ManyToManyField('TimeToRun')

	def __unicode__(self):
		return self.username

class TimeToRun(models.Model):
	time_string = models.CharField(max_length=255)

	def hour_in_day(self):
		return time.strptime(self.time_string, "%I:00 %p").tm_hour

	def __unicode__(self):
		return self.time_string
