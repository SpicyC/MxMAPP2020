from __future__ import unicode_literals

from django.contrib import admin

from .models import Event

# Register your models here.

admin.site.register(Event)

#class EventAdmin(admin.ModelAdmin):
#      list_display = ['day', 'start_time', 'end_time', 'notes']
