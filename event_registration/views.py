from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import RegisteredEvent
from events.models import Event

from django.views.decorators.csrf import csrf_protect



from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import mixins
from rest_framework import generics
from event_registration.serializer import RegSerializer



# Create your views here.







@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Registered Event': reverse('registered-events', request=request, format=format),
        
    })





class RegEvents(generics.ListCreateAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = RegisteredEvent.objects.all()
    serializer_class = RegSerializer



    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    



class RegDetail(generics.RetrieveUpdateDestroyAPIView, mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = RegisteredEvent.objects.all()
    serializer_class = RegSerializer
    


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)






























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