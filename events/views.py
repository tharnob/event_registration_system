from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Event
from django.views.decorators.csrf import csrf_protect

# Create your views here.

def home(request):
    event = Event.objects.all().values()
    template = loader.get_template('dashboard.html')
    context = {
        "event": event,
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def add_event(request):
    if request.method == 'POST':
        print("Added")

        #retreive the user inputs
        title = request.POST.get("title")
        description = request.POST.get("description")
        event_date = request.POST.get("event_date")
        event_time = request.POST.get("event_time")
        location_name = request.POST.get("location_name")
        
    

        #create an object for models
        s = Event()
        s.title=title
        s.description=description
        s.event_date=event_date
        s.event_time=event_time
        s.location_name=location_name
        

        s.save()
        return redirect("/dashboard")


    template = loader.get_template("add_event.html")
    context = {'some_key': 'some_value'}
    return HttpResponse(template.render(context, request))




def delete_event(request, id):
    s = Event.objects.get(pk=id)
    s.delete()

    return redirect("/dashboard")


def update_event(request, id):
    s = Event.objects.get(pk=id)

    template = loader.get_template("update_event.html")
    context = {'event': s}
    return HttpResponse(template.render(context, request))


def do_update_event(request, id):
    title = request.POST.get("title")
    description = request.POST.get("description")
    event_date = request.POST.get("event_date")
    event_time = request.POST.get("event_time")
    location_name = request.POST.get("location_name")


    s = Event.objects.get(pk=id)
    s.title=title
    s.description=description
    s.event_date=event_date
    s.event_time=event_time
    s.location_name=location_name

    s.save()
    return redirect("/dashboard")
