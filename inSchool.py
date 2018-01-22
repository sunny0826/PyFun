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
from proBability import random_pick

'''事件'''
def inSchool(itime):
    events = event()
    if events=='chinese':
        print('chinese class')
    elif events=='math':
        print('math class')
    elif events == 'english':
        print('english class')
    elif events == 'biology':
        print('biology class')
    else:
        print("!!!!!!")
    when = itime - 1
    print(when)
    if when < 0:
        return -1
    timer = threading.Timer(1, inSchool,[when])
    timer.start()

'''概率调整'''
def event():
    event_list = ['chinese', 'math', 'english','biology']
    probabilities = [0.2, 0.3, 0.3, 0.2]
    events = random_pick(event_list, probabilities)
    return events

if __name__ == '__main__':
    timer = threading.Timer(1, inSchool,[8])
    timer.start()