from django.contrib import admin
from models import TwitterAccount

class TwitterAccountAdmin(admin.ModelAdmin):
	list_display = ['username']

admin.site.register(TwitterAccount, TwitterAccountAdmin)
