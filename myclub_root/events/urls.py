from django.urls import path, re_path # Add re_path to the import statement
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gentext/', views.gen_text, name='generate-text-file'),
    path('gencsv/', views.gen_csv, name='generate-csv-file'),
    path('genjson/', views.gen_json, name='generate-json'),
    path('genpdf/', views.gen_pdf, name='generate-pdf-file'),
    path('getsubs/', views.list_subscribers, name='list-subscribers'),
    path('add_venue/', views.add_venue, name='add-venue'), # Add a URL pattern for the add_venue view
    path('events/', views.all_events, name='show-events'), # Add a URL pattern for the all_events view
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/$', views.index, name='index'), # Use re_path to capture year and month   
]