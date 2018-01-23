#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong
'''
1h=3600s
chinese:0.45h
math:0.45h
english:0.45h
biology:0.45h
 '''
import threading
import logging
from logging.config import fileConfig

import gameMain
from proBability import random_pick

'''配置日志'''
fileConfig('./log/logging.conf')
logger=logging.getLogger('infoLogger')

'''事件'''
def inSchool(itime):
    events = event()
    when = itime - 1
    if events=='chinese':
        logging.info('CHINESE class, remaining '+str(when)+'h')
    elif events=='math':
        logging.info('MATH class, remaining '+str(when)+'h')
    elif events == 'english':
        logging.info('ENGLISH class, remaining '+str(when)+'h')
    elif events == 'biology':
        logging.info('BIOLOGY class, remaining '+str(when)+'h')
    timer = threading.Timer(1, inSchool,[when])
    while when<0:
        timer.cancel()
        gameMain.fun_timer()
    timer.start()

'''概率调整'''
def event():
    event_list = ['chinese', 'math', 'english','biology']
    probabilities = [0.2, 0.3, 0.3, 0.2]
    events = random_pick(event_list, probabilities)
    return events
#
# if __name__ == '__main__':
#     timer = threading.Timer(1, inSchool,[8])
#     timer.start()