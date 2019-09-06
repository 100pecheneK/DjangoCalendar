from django.shortcuts import render

from .models import Events

from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
import datetime

from django.contrib.auth.models import User

# from django.contrib.auth.decorators import login_required
# @login_required

# Отображает все ивенты пользователя
def events(request):
    # Пользователь авторизован.
    now = datetime.datetime.now()
    events = Events.objects.filter(author=request.user)[::-1]
    return render(request, 'calendarV2/events.html', {"events": events, "now": now})


def eventsCreate(request):

    user = User.objects.get(username=request.user)
    user.events_set.create(title=request.POST['title'], dateStart=request.POST['dateStart'])

    # return HttpResponseRedirect(reverse('calc:events'))
    return HttpResponseRedirect(reverse('calc:events'))

def eventDelete(request, event_id):
    try:
        event = Events.objects.get(id = event_id)
        event.delete()
    except:
        raise Http404("Событие не найдено")
    return HttpResponseRedirect(reverse('calc:events'))

def eventsDelete(request):
    try:
        events = Events.objects.filter(author=request.user)
        events.delete()
    except:
        raise Http404("Событие не найдено")
    return HttpResponseRedirect(reverse('calc:events'))