from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import date
import calendar # Import the calendar module
from calendar import HTMLCalendar # Import the HTMLCalendar class

from .models import Event  # Import the Event model
from .forms import VenueForm  # Import the VenueForm class

def index(request, year=date.today().year, month=date.today().month): # Add year and month default parameters
    #  t = date.today() # Assign today's date
    #  month = t.strftime('%b') # Format the month
    #  year = t.year # Assign the year
    year = int(year) # Convert year to integer
    month = int(month) # Convert month to integer
    if year < 2000 or year > 2099: year = date.today().year
    month_name = calendar.month_name[month] # Get the full month name
    # title = f'MyClub Event Calendar - {month} {year}'
    title = f'MyClub Event Calendar - {month_name} {year}'
    cal = HTMLCalendar().formatmonth(year, month) # Create an HTML calendar for the given month and year

    # Hardcoded announcements for demonstration purposes
    announcements = [
            {
                'date': '10-10-2026',
                'announcement': "Club Registrations Open"
            },
            {
                'date': '07-15-2026',
                'announcement': "Joe Smith Elected New Club President"
            }
        ]
    
    # return HttpResponse(f"<h1>{title}</h1>")
    # return HttpResponse(f"<h1>{title}</h1><p>{cal}</p>")
    return render(request, 
        'events/calendar_base.html', 
        {"title": title,"cal": cal, "announcements": announcements }
        ) # Render the base.html template with the title and calendar

def all_events(request):
    event_list = Event.objects.all()
    return render(request,
        'events/event_list.html',
        {'event_list': event_list}
    )

def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue/?submitted=True')
    else:
        form = VenueForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 
        'events/add_venue.html', 
        {'form': form, 'submitted': submitted}
        )