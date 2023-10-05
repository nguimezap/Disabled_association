from django.db import models

# Create your models here.

# association/models.py

from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    disability_type = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()
    # Add more fields as needed


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    location = models.CharField(max_length=200)
    event_type = models.CharField(max_length=50)
    organizer = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='events_organized')
    attendees = models.ManyToManyField(Member, related_name='events_attending', blank=True)
    # Add more fields as needed

    def __str__(self):
        return self.title
