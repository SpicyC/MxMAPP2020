"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from myapp import views as profile_views


from events.views import CalendarView


    


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', profile_views.index, name='list_profiles'),

    path('profiles/add_profiles', profile_views.add_profiles, name='add_profiles'),

    path('profiles/<int:pk>/delete/', profile_views.delete_profile, name='delete_profile'),

    path('profiles/<int:pk>/edit/', profile_views.edit_profiles, name='edit_profiles'),

    path('profiles/<int:pk>/detail/', profile_views.profiles_detail, name='profiles_detail'), 


    path('', CalendarView.as_view(),
    name='calendarview'),


]
