from django import template
from django.utils.html import format_html # Import format_html for safe HTML rendering
from django.template.defaultfilters import stringfilter
from datetime import datetime

register = template.Library()

@register.filter(name='reverse')
@stringfilter
def reverse(value):
    return value[::-1]

@register.simple_tag
def create_date(date_val):
    return "This content was created on %s" % date_val.strftime('%A %B %d, %Y')

@register.simple_block_tag
def highlight(content, color='yellow'):
    return format_html('<span style="background-color: {}">{}</span>', color, content)

@register.inclusion_tag('events/announcements.html')
def announcements():
    announcements = [
        {
            'date': '6-10-2026',
            'announcement': "Club Registrations Open"
        },
        {
            'date': '6-15-2026',
            'announcement': "Joe Smith Elected New Club President"
        }
    ]
    return {'announcements': announcements}