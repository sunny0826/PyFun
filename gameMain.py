#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong
import threading

from inHome import inHome
from inSchool import inSchool
from onTour import onTour
from proBability import random_pick
from timer import momentInDay


def fun_timer():
    #配置概率
    event_list = ['home', 'school', 'tour']
    probabilities = [0.2, 0.2, 0.6]
    site = random_pick(event_list, probabilities)
    print(site)
    alt_list = [6, 8, 10, 12, 24]
    probabilities = [0.1, 0.3, 0.5, 0.1]
    alt_time = random_pick(alt_list, probabilities)
    print(alt_time)
    # goTo(site,alt_time)
    global timer
    timer = threading.Timer(5, fun_timer)
    timer.start()

def goTo(site,atime):
    if site=='tour':
        onTour(atime)
    elif site=='home':
        inHome(atime)
    elif site=='school':
        inSchool(atime)

timer = threading.Timer(1, fun_timer)
timer.start()

