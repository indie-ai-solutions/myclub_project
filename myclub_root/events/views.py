from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar # Import the calendar module
from calendar import HTMLCalendar # Import the HTMLCalendar class

def index(request, year=date.today().year, month=date.today().month): # Add year and month default parameters
    #  t = date.today() # Assign today's date
    #  month = date.strftime(t, '%b') # Format the month
    #  year = t.year # Assign the year
    year = int(year) # Convert year to integer
    month = int(month) # Convert month to integer
    if year < 1900 or year > 2099: year = date.today().year
    month_name = calendar.month_name[month] # Get the full month name
    title = "MyClub Event Calendar - %s %s" % (month_name, year)
    cal = HTMLCalendar().formatmonth(year, month) # Create an HTML calendar for the given month and year
    
    # return HttpResponse("<h1>%s</h1>" % title)
    return HttpResponse("<h1>%s</h1><p>%s</p>" % (title, cal)) # Return the title and calendar as an HTTP response
