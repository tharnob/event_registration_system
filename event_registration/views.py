from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import RegisteredEvent
from events.models import Event
from django.views.decorators.csrf import csrf_protect

# Create your views here.

def event_registration_page(request, id):
    reg_event = RegisteredEvent.objects.all().values()
    # reg_event = RegisteredEvent.objects.get(pk=id)
    event = Event.objects.get(pk=id)
    template = loader.get_template('event_registration.html')
    context = {
        "reg_event": reg_event,
        "event": event,
    }
    return HttpResponse(template.render(context, request))


@csrf_protect
def event_registration(request):
    if request.method == 'POST':
        print("Added")

        #retreive the user inputs
        event_id = request.POST.get("event_id")
        event_title = request.POST.get("event_title")
        user_name = request.POST.get("user_name")
        slot = request.POST.get("slot")
        slot = int(slot) - 1
        
        

        
    

        #create an object for models
        s = RegisteredEvent()
        k = Event.objects.get(pk=event_id)
        s.event_id=event_id
        s.event_title=event_title
        s.user_name=user_name
        k.slot=slot

     
        

        s.save()
        k.save()
        return redirect("/dashboard")


    template = loader.get_template("event_registration.html")
    context = {'some_key': 'some_value'}
    return HttpResponse(template.render(context, request))



def registered_event(request):

    reg_event = RegisteredEvent.objects.all().values()
    event = Event.objects.all().values()
    # reg_event = RegisteredEvent.objects.get(pk=id)
    
    template = loader.get_template('registered_event.html')
    context = {
        "reg_event": reg_event,
        "event": event,
        
    }
    return HttpResponse(template.render(context, request))



def delete_registration(request, id):
    s = RegisteredEvent.objects.get(pk=id)
    reg_details = RegisteredEvent.objects.get(pk=id)
    e_id = reg_details.event_id
    k = Event.objects.get(pk=e_id)
    k.slot = k.slot + 1
    k.save()
    s.delete()

    return redirect("/events/registered_event/")