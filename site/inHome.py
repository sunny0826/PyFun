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
import logging
import threading
from logging.config import fileConfig

from control.proBability import random_pick
from control.timer import momentInDay
from gameMain import fun_timer

'''配置日志'''
fileConfig('./log/logging.conf')
logger=logging.getLogger('infoLogger')

'''事件'''
def inHome(itime):
    events = event()
    if events=='game':
        when = itime - 2
        timer = threading.Timer(2, inHome,[when])
        logging.info('start GAME, remaining '+str(when)+'h')
        if when<0:
            timer.cancel()
            fun_timer()
        timer.start()
    elif events=='read':
        when = itime - 1
        logging.info('start READ, remaining '+str(when)+'h')
        timer = threading.Timer(1, inHome,[when])
        if when < 0:
            timer.cancel()
            fun_timer()
        timer.start()
    elif events == 'sleep':
        when = itime - 8
        logging.info('start SLEEP, remaining '+str(when)+'h')
        timer = threading.Timer(8, inHome,[when])
        if when < 0:
            timer.cancel()
            fun_timer()
        timer.start()
    elif events == 'eat':
        when = itime - 0.5
        logging.info('start EAT, remaining '+str(when)+'h')
        timer = threading.Timer(0.5, inHome,[when])
        if when < 0:
            timer.cancel()
            fun_timer()
        timer.start()
    elif events == 'handwork':
        when = itime - 2
        timer = threading.Timer(2, inHome,[when])
        logging.info('start SSR event: HANDWORK!, remaining '+str(when)+'h')
        if when < 0:
            timer.cancel()
            fun_timer()
        timer.start()

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

# if __name__ == '__main__':
#     timer = threading.Timer(1, inHome,[24])
#     timer.start()