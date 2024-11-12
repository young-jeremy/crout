from django import template
from django.utils.timesince import timesince
from django.utils import timezone

register = template.Library()

@register.filter
def main_unit_timesince(date):
    # Ensure the date is timezone-aware (or naive, depending on your project)
    if date.tzinfo is None:
        date = timezone.make_aware(date, timezone.get_current_timezone())  # Make it aware if it's naive
    elif date.tzinfo is not None:
        date = date.astimezone(timezone.utc).replace(tzinfo=None)  # Convert to naive if it's aware

    # Convert timezone-aware current time to naive if needed
    current_time = timezone.now()
    if current_time.tzinfo is not None:
        current_time = current_time.astimezone(timezone.utc).replace(tzinfo=None)

    # Now we can safely subtract the date from the current time
    timesince_str = timesince(date, current_time)

    # Return the first part of the timesince string (e.g., "3 days ago")
    return timesince_str.split(",")[0]
