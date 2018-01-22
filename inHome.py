#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong
'''
1h=3600s
game:2h
read:1h
sleep:8h
eat:0.5h
handwork:2h
 '''
import threading
import time
from proBability import random_pick
from timer import momentInDay

'''事件'''
def inHome(itime):
    events = event()
    if events=='game':
        print('start game')
        when = itime - 2
        print(when)
        if when<0:
            return -1
        # time.sleep(2)
        # inHome(when)
        timer = threading.Timer(3600*2, inHome,[when])
        timer.start()
    elif events=='read':
        print('start read')
        when = itime - 1
        print(when)
        if when < 0:
            return -1
        # time.sleep(1)
        # inHome(when)
        timer = threading.Timer(3600, inHome,[when])
        timer.start()
    elif events == 'sleep':
        print('start sleep')
        when = itime - 8
        print(when)
        if when < 0:
            return -1
        # time.sleep(8)
        # inHome(when)
        timer = threading.Timer(3600*8, inHome,[when])
        timer.start()
    elif events == 'eat':
        print('start eat')
        when = itime - 0.5
        print(when)
        if when < 0:
            return -1
        # time.sleep(0.5)
        # inHome(when)
        timer = threading.Timer(3600*0.5, inHome,[when])
        timer.start()
    elif events == 'handwork':
        print('start handwork')
        when = itime - 2
        print(when)
        if when < 0:
            return -1
        # time.sleep(0.5)
        # inHome(when)
        timer = threading.Timer(3600*2, inHome,[when])
        timer.start()
    else:
        print("!!!!!!")

'''概率调整'''
def event():
    eventTime = momentInDay()
    event_list = ['game', 'read', 'sleep', 'eat', 'handwork']
    if eventTime in ['foredawn','dawn']:
        probabilities = [0.3, 0, 0.6, 0.1,0]
    elif eventTime in ['morning','forenoon']:
        probabilities = [0.1, 0.3, 0.59, 0.1, 0.01]
    elif eventTime in ['noon','afternoon','dusk','midnight']:
        probabilities = [0.28, 0.2, 0.1, 0.4, 0.02]
    events = random_pick(event_list, probabilities)
    return events

if __name__ == '__main__':
    timer = threading.Timer(1, inHome,[24])
    timer.start()