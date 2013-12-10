from django.db import models

# Create your models here.
class TwitterAccount(models.Model):
	username = models.TextField()

	twitter_consumer_key = models.CharField(max_length=255)
	twitter_consumer_secret = models.CharField(max_length=255)
	twitter_access_token = models.CharField(max_length=255)
	twitter_access_token_secret = models.CharField(max_length=255)

	tweet_frequency = models.IntegerField('Tweets per day')

	hours_allowed = models.ManyToManyField('HourAllowed')

class HourAllowed(models.Model):
	hour = models.CharField(max_length=255)

	def __unicode__(self):
		return self.hour
