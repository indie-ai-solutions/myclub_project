from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from .models import Event, Venue, MyClubUser # Register models
from events.forms import VenueForm # Import custom form for Venue model

class EventsAdmin(AdminSite):
    site_header = 'MyClub Events Administration'
    site_title = 'MyClub Events Admin'
    index_title = 'MyClub Events Admin Home'

class EventInline(admin.StackedInline):
    model = Event
    fields = ('name', 'event_date')
    extra = 1

class AttendeeInline(admin.TabularInline):
    model = Event.attendees.through
    verbose_name = 'Attendee'
    verbose_name_plural = 'Attendees'

admin_site = EventsAdmin(name='eventsadmin')

@admin.register(Venue, site=admin_site) # Register Venue model with custom admin site
class VenueAdmin(admin.ModelAdmin):
    form = VenueForm # Use custom form for Venue model
    list_display = ('name', 'address', 'phone')
    # list_display_links = ('name', 'address') # Make name and address clickable in list view
    # list_editable = ('phone',) # Allow phone field to be editable in list view
    # list_display_links = None # Disable clickable links in list view
    # list_editable = list_display # Allow all fields to be editable in list view
    ordering = ('name',)
    search_fields = ('name', 'address')
    # inlines = [
    #     EventInline,
    # ] # Display related events inline in Venue admin

    def get_list_display(self, request):
        return ('name', 'address', 'phone', 'web')

@admin.action(description="Manage selected events")
def set_manager(modeladmin, request, queryset):
    queryset.update(manager=request.user)

@admin.register(Event, site=admin_site) # Register Event model with custom admin site
class EventAdmin(admin.ModelAdmin):
    # fields = (('name','venue'), 'event_date', 'description', 'manager')
    list_display = ('name', 'event_date', 'venue', 'manager')
    list_filter = ('event_date', 'venue')
    ordering = ('-event_date',)
    actions = [set_manager] # Add custom action to set manager for selected events
    save_as = True # Allow saving as a new object
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
    inlines = [
        AttendeeInline,
    ] # Display related attendees inline in Event admin

# admin.site.register(Venue)
admin.site.register(MyClubUser)
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
# admin.site.register(Event)