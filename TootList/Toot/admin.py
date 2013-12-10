from django.contrib import admin
from models import Toot

# Register your models here.
class TootAdmin(admin.ModelAdmin):
	list_display = ['text', 'pub_date']

admin.site.register(Toot, TootAdmin)
