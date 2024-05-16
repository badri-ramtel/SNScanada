from django.shortcuts import render, redirect
from event_app.models import CreateEvent, Event
from team_app.models import Year_Book
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def events(request):
    eventor = request.GET.get('eventor')
    if eventor == None:
        events = Event.objects.all()
    else: 
        events = Event.objects.filter(created_events__event_name= eventor) 

    eventor = CreateEvent.objects.all() 
    committee = Year_Book.objects.all()
    paginator = Paginator(events,3)
    page_number = request.GET.get('page')
    try: 
        page_obj = paginator.get_page(page_number)

    except PageNotAnInteger:
        page_obj = paginator.page(1)

    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {'eventor': eventor, 'page_obj': page_obj, 'committee': committee}
    return render(request, 'event_app/event.html', context)
 
def viewEvent(request, pk):
    events_name = CreateEvent.objects.all()
    event = Event.objects.get(id= pk)
    committee = Year_Book.objects.all()
    context = {'events_name': events_name, 'event': event, 'committee': committee}
    return render(request, 'event_app/viewevent.html', context)          
