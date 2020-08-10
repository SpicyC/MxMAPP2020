from django.shortcuts import render, redirect, get_object_or_404

from django.http import JsonResponse

from .models import Profile

from .forms import profileForm

#Calendar Views
from datetime import datetime

from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from events.utils import Calendar

# Create your views here.





def index(request):
  all_profiles = Profile.objects.all().order_by('name')
  
  return render(request, 'profiles/list_profiles.html', context={'profiles':all_profiles})
  

def add_profiles(request):
    if request.method == 'GET':
        form = profileForm()
    else:
        form = profileForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_profiles')

    return render(request, "profiles/add_profiles.html", {"form": form})

def delete_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        
        return JsonResponse({"deleted": 'true'})
        


def profiles_detail(request, pk):
  profile = get_object_or_404(Profile, pk=pk)
  return render(request, "profiles/profiles_detail.html", {"profile": profile})





def edit_profiles(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'GET':
        form = profileForm(instance=profile)
    else:
        form = profileForm(data=request.POST, instance=profile)
        
        if form.is_valid():
            form.save()
            return redirect(to='list_profiles')

    return render(request, "profiles/edit_profiles.html", {
        "form": form, "profile": profile})



#Calendar Views



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
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()