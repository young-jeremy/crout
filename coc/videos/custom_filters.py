from django import template
from django.utils.timesince import timesince
from datetime import datetime

register = template.Library()

@register.filter
def main_unit_timesince(date):
    # Get the timesince string (e.g., "3 months, 2 weeks")
    timesince_str = timesince(date, datetime.now())
    # Split and return only the main unit (e.g., "3 months")
    return timesince_str.split(",")[0]
