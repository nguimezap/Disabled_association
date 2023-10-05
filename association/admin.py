from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Member, Event

# Custom Admin class for Member
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'disability_type', 'email', 'phone_number')
    list_filter = ('disability_type',)  # Add more fields as needed
    search_fields = ('name', 'email')  # Add more fields as needed

# Custom Admin class for Event
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'event_type', 'organizer')
    list_filter = ('event_type',)  # Add more fields as needed
    search_fields = ('title', 'organizer__name')  # Add more fields as needed
    date_hierarchy = 'date'  # Add a date-based drilldown navigation

    # Customize the form to handle attendees (many-to-many)
    filter_horizontal = ('attendees',)

# Register the custom admin classes
admin.site.register(Member, MemberAdmin)
admin.site.register(Event, EventAdmin)
