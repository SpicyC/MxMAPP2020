from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()



    # day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    # start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    # end_time = models.TimeField(u'Final time', help_text=u'Final time')
    # notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)
 
    # class Meta:
    #     verbose_name = u'Scheduling'
    #     verbose_name_plural = u'Scheduling'