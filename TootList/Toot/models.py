from django.db import models
from TwitterAccount.models import TwitterAccount
from django.core.validators import MaxLengthValidator
import math, random, time, datetime, calendar
from TwitterAccount.models import TwitterAccount, TimeToRun

class Toot(models.Model):
	account = models.ForeignKey(TwitterAccount, default=1)

	text = models.TextField(validators=[MaxLengthValidator(140)])

	def get_next_available_datetime():
		account = TwitterAccount.objects.all()[0] # for now

		if len(Toot.objects.all()) == 0:
			# if no toots are scheduled, start with tomorrow
			next_avail_date = datetime.date.today() + datetime.timedelta(days=1)
		else:
			# find the last day a toot is scheduled
			latest = Toot.objects.all().order_by('-pub_date')[0].pub_date
			num_on_latest_day = len(Toot.objects.all().filter(pub_date__year=latest.year,pub_date__month=latest.month,pub_date__day=latest.day))
			# if there are < tweet_frequency, use that day
			if num_on_latest_day < account.tweet_frequency:
				next_avail_date = latest
			else:
				# otherwise, our day is the day after that one
				next_avail_date = latest + datetime.timedelta(days=1)
		
		# now get an hour+minute
		allowed_hours = account.times_to_run.all()
		random_allowed_hour = allowed_hours[int(math.floor(random.random() * len(allowed_hours)))].hour_in_day()
		random_minute = int(math.floor(random.random() * 60))
		# return as object
		return next_avail_date.replace(hour=random_allowed_hour, minute=random_minute)

	# BUG: get_next_available_datetime is working correctly, but the default isn't getting set correctly.
	pub_date = models.DateTimeField('Publish DateTime', default=get_next_available_datetime)

	def __unicode__(self):
		return self.text[:70] + (self.text[70:] and '...')
		
	class Meta:
		ordering = ['pub_date']