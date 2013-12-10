from django.contrib import admin
from models import Toot

# Register your models here.
class TootAdmin(admin.ModelAdmin):
	list_display = ['pub_date', 'text']

admin.site.register(Toot, TootAdmin)
