from .utils import Calendar

from .models import Event

class CalendarView():
    model = Event
    template_name = 'components/calendar.html'
    #success_url = reverse_lazy("calendar")

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
    
        d = get_date(self.request.GET.get('month', None))
    
        cal = Calendar(d.year, d.month)
    
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)

        return context



