from django.urls import path, re_path # Add re_path to the import statement
from django.views.generic.base import TemplateView, RedirectView # Import TemplateView and RedirectView
from django.views.generic.dates import ArchiveIndexView
from . import views
from events.views import ArchiveIndexViewDemo, MonthArchiveViewDemo # Import the class-based views
from events.views import TemplateViewDemo, ListViewDemo, DetailViewDemo, CreateViewDemo, UpdateViewDemo, DeleteViewDemo # Import the class-based views
from .models import Event

urlpatterns = [
    path('', views.index, name='index'),
    # path('eventarchive/', ArchiveIndexView.as_view(model=Event, date_field='event_date'), name='event-index'),
    path('eventarchive/', ArchiveIndexViewDemo.as_view(), name='event-index'), # Use the ArchiveIndexViewDemo class-based view
    path('home/', RedirectView.as_view(url='/', permanent=True)), # Add a URL pattern for the RedirectView to redirect /home/ to /
    path('cbvdemo/', TemplateViewDemo.as_view(), name='cbvdemo'), # Add a URL pattern for the TemplateViewDemo class-based view
    path('condemo/', views.context_demo, name='condemo'),
    path('tdemo/', views.template_demo, name='tdemo'), # Add a URL pattern for the template_demo view
    path('gentext/', views.gen_text, name='generate-text-file'),
    path('gencsv/', views.gen_csv, name='generate-csv-file'),
    path('genjson/', views.gen_json, name='generate-json'),
    path('genpdf/', views.gen_pdf, name='generate-pdf-file'),
    path('getsubs/', views.list_subscribers, name='list-subscribers'),
    path('add_venue/', views.add_venue, name='add-venue'), # Add a URL pattern for the add_venue view
    # path('events/', views.all_events, name='show-events'),
    path('events/', ListViewDemo.as_view(), name='show-events'), # Use ListViewDemo class-based view for /events/ URL
    path('event/<int:pk>/', DetailViewDemo.as_view(), name='event-detail'), # Use DetailViewDemo class-based view for /event/<int:pk>/ URL
    path('event/add/', CreateViewDemo.as_view(), name='add-event'), # Use CreateViewDemo class-based view for /event/add/ URL
    path('event/update/<int:pk>/', UpdateViewDemo.as_view(), name='update-event'), # Use UpdateViewDemo class-based view
    path('event/delete/<int:pk>/', DeleteViewDemo.as_view(), name='delete-event'), # Use DeleteViewDemo class-based view
    path('events/<int:year>/<int:month>/', MonthArchiveViewDemo.as_view(), name='event-montharchive'), # Use MonthArchiveViewDemo class-based view
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/$', views.index, name='index'), # Use re_path to capture year and month   
]