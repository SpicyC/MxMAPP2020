from __future__ import unicode_literals

from django.db import models

from django.views import generic

from django.utils.safestring import mark_safe


from django.urls import reverse

import datetime, timedelta


from calendar import HTMLCalendar
# from .models import Event

# # from .models import Event
# from .utils import Calendar

# # Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200)
    
    description = models.TextField()
    
    start_time = models.DateTimeField(default=datetime.date.today)
    
    end_time = models.DateTimeField()

    day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    
    end_time = models.TimeField(u'Final time', help_text=u'Final time')
    
    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)
 
    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'

    def __str__(self):
        return self.title


# class CalendarView(generic.ListView):
#     model = Event
#     template_name = 'events/calendar.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         # use today's date for the calendar
#         d = get_date(self.request.GET.get('day', None))

#         #Instantiate our calendar class with today's year and date
#         events = Calendar(d.year, d.month)

#         # Call the formatmonth method, which returns our calendar as a table
#         html_events = events.formatmonth(withyear=True)
#         context['events/calendar.html'] = mark_safe(html_events)
#         return context


class CalendarView(generic.ListView):
    model = Event
    template_name = 'events/calendar.html'

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

        # use today's date for the calendar
    d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
    events = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
    html_events = events.formatmonth(withyear=True)
    context['calendar'] = mark_safe(html_events)
    context['prev_month'] = prev_month(d)
    context['next_month'] = next_month(d)
    return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
    return date(year, month, day=1)
    return datetime.today()

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
        return datetime.today()



class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		d = ''
		for event in events_per_day:
			d += f'<li> {event.title} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr 
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

# formats a month as a table filter events by year and month

def formatmonth(self, withyear=True):
    events = self.Event.objects.filter(start_time__year=self.year, start_time__month=self.month)
    events = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
    events += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
    events += f'{self.formatweekheader()}\n'
    for week in self.monthdays2calendar(self.year, self.month): events += f'{self.formatweek(week, events)}\n'
    return events