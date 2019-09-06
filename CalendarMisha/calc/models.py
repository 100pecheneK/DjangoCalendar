from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime

import json


class Events(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    dateStart = models.DateField(default=timezone.now)

    def get_dateStart(self):        
        return self.dateStart.strftime("%Y-%m-%d")

    def will_it_be_soon(self):
        return timezone.now().date() <= self.dateStart <= (timezone.now().date() + datetime.timedelta(days = 7))

    def __str__(self):
        return self.title
