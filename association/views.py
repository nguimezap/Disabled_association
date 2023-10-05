
# association/views.py

from django.shortcuts import render
from .models import Member, Event
from django.shortcuts import render
from django.http import HttpResponseRedirect




from django.shortcuts import render, redirect, get_object_or_404
from .models import Member, Event
from .forms import MemberForm, EventForm  # Import forms for creating and updating records

# View to list all members
def member_list(request):
    members = Member.objects.all()
    return render(request, 'association/member_list.html', {'members': members})
    

# View to view details of a single member
def member_detail(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    return render(request, 'association/member_detail.html', {'member': member})

# View to create a new member
def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'association/member_form.html', {'form': form})

# View to update an existing member
def member_update(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'association/member_form.html', {'form': form})

# View to delete a member
def member_delete(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        member.delete()
        return redirect('member_list')
    return render(request, 'association/member_confirm_delete.html', {'member': member})

# Similar views for Event model (list, detail, create, update, delete)
# Be sure to define corresponding HTML templates and forms

# View to list all events
def event_list(request):
    events = Event.objects.all()
    return render(request, 'association/event_list.html', {'events': events})

# View to view details of a single event
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'association/event_detail.html', {'event': event})

# View to create a new event
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'association/event_form.html', {'form': form})

# View to update an existing event
def event_update(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'association/event_form.html', {'form': form})

# View to delete an event
def event_delete(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'association/event_confirm_delete.html', {'event': event})



def index(request):
    return render(request, 'association/index.html')  



def qui_sommes_nous(request):
    return render(request, 'association/qui_sommes_nous.html')




def faire_un_don(request):
    # You can add any necessary logic here
    return render(request, 'association/faire_un_don.html')  



def nous_contacter(request):
    # You can add any necessary logic here
    return render(request, 'association/nous_contacter.html')



def carriere(request):
    # You can add any necessary logic here
    return render(request, 'association/carriere.html')


def register_event(request):
    if request.method == 'POST':
        # Process the form data here
        full_name = request.POST.get('full-name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comments = request.POST.get('comments')
        
        # You can save the data to your database or perform other actions here

        # Redirect to a thank you page or a confirmation page
        return HttpResponseRedirect('/thank-you/')  # Update the URL as needed

    return render(request, 'association/registration_page.html')



from django.shortcuts import render

def actualites(request):
    # Add logic to fetch news articles or data if needed
    news_articles = [
        {
            'title': 'Titre de l\'article 1',
            'date': '1er Octobre 2023',
            'content': 'Ceci est un résumé de l\'article 1. Vous pouvez ajouter des détails sur l\'événement ou la nouvelle ici.',
        },
        {
            'title': 'Titre de l\'article 2',
            'date': '15 Septembre 2023',
            'content': 'Ceci est un résumé de l\'article 2. Vous pouvez ajouter des détails sur l\'événement ou la nouvelle ici.',
        },
        # Add more news articles as needed
    ]

    return render(request, 'association/actualites.html', {'news_articles': news_articles})




def evenements(request):
    # Add logic to fetch event data if needed
    events = [
        {
            'title': 'Événement 1',
            'date': 'Date de l\'événement 1',
            'location': 'Lieu de l\'événement 1',
            'description': 'Description de l\'événement 1. Vous pouvez ajouter des détails sur l\'événement ici.',
        },
        {
            'title': 'Événement 2',
            'date': 'Date de l\'événement 2',
            'location': 'Lieu de l\'événement 2',
            'description': 'Description de l\'événement 2. Vous pouvez ajouter des détails sur l\'événement ici.',
        },
        # Add more events as needed
    ]

    return render(request, 'association/evenements.html', {'events': events})
