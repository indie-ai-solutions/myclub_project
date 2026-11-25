from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from .models import Event, Venue, MyClubUser # Register models

class EventsAdmin(AdminSite):
    site_header = 'MyClub Events Administration'
    site_title = 'MyClub Events Admin'
    index_title = 'MyClub Events Admin Home'

admin_site = EventsAdmin(name='eventsadmin')

@admin.register(Venue, site=admin_site) # Register Venue model with custom admin site
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')

@admin.register(Event, site=admin_site) # Register Event model with custom admin site
class EventAdmin(admin.ModelAdmin):
    # fields = (('name','venue'), 'event_date', 'description', 'manager')
    list_display = ('name', 'event_date', 'venue')
    list_filter = ('event_date', 'venue')
    ordering = ('-event_date',)
    fieldsets = (
        ('Required Information', {
            'description': "These fields are required for each event.",
            'fields': (('name','venue'), 'event_date')
        }),
        ('Optional Information', {
            'classes': ('collapse',),
            'fields': ('description', 'manager')
        }),
    )

# admin.site.register(Venue)
admin.site.register(MyClubUser)
admin_site.register(User)
admin_site.register(Group)
# admin.site.register(Event)