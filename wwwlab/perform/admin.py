'''
Created on Oct 24, 2013

@author: alice
'''
from django.contrib import admin
from models import Experiment, Trial, Event

admin.site.register(Experiment)
admin.site.register(Trial)
admin.site.register(Event)