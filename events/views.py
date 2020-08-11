# from django.shortcuts import render

# from django.http import HttpResponse

# Create your views here.

#def index(request):
#     return HttpResponse('hello')

from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from django.urls import reverse

# from .utils import Calendar

from .models import Event, CalendarView, Calendar


def events (request):
    return render(request, 'events/calendar.html')


# class CalendarView(generic.ListView):
#     model = Event
#     template_name = 'events/calendar.html'

# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)

#         # use today's date for the calendar
#     d = get_date(self.request.GET.get('day', None))

#         # Instantiate our calendar class with today's year and date
#     events = Calendar(d.year, d.month)

#         # Call the formatmonth method, which returns our calendar as a table
#     html_events = events.formatmonth(withyear=True)
#     context['calendar'] = mark_safe(html_events)
#     context['prev_month'] = prev_month(d)
#     context['next_month'] = next_month(d)
#     return context

# def get_date(req_day):
#     if req_day:
#         year, month = (int(x) for x in req_day.split('-'))
#     return date(year, month, day=1)
#     return datetime.today()


