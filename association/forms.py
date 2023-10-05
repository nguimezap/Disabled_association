# association/forms.py

from django import forms
from .models import Member, Event

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'disability_type', 'email', 'phone_number', 'address', 'date_of_birth']
        # You can include additional fields from your Member model as needed

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'description', 'location', 'event_type', 'organizer', 'attendees']
        # You can include additional fields from your Event model as needed
