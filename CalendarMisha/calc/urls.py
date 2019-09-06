from django.urls import path
from . import views


app_name = 'calc'

urlpatterns = [
    path('calendar', views.events, name='events'),
    path('calendar/create', views.eventsCreate, name='eventsCreate'),
    path('calendar/delete/<int:event_id>', views.eventDelete, name='eventDelete'),
    path('calendar/deleteALL', views.eventsDelete, name='eventDeleteALL'),
]