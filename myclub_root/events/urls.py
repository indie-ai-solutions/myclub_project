from django.urls import path, re_path # Add re_path to the import statement
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.all_events, name='show-events'), # Add a URL pattern for the all_events view
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/', views.index, name='index'), # Use re_path to capture year and month   
]