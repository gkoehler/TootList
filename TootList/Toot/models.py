from django.db import models

# Create your models here.
class Toot(models.Model):
	text = models.TextField()
	pub_date = models.DateField('Date Published')
	published = models.BooleanField()

	class Meta:
		ordering = ['-pub_date']
