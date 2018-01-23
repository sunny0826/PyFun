#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong
import inHome
from inSchool import inSchool
from onTour import onTour
from proBability import random_pick
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %a %H:%M:%S',
    )

def fun_timer():
    #配置概率
    event_list = ['home', 'school', 'tour']
    probabilities = [0.6, 0.4, 0]
    site = random_pick(event_list, probabilities)
    alt_list = [6, 8, 10, 12, 24]
    probabilities = [0.1, 0.3, 0.5, 0.1]
    alt_time = random_pick(alt_list, probabilities)
    logging.warning('site：'+site+'，at least:'+str(alt_time)+'h')#打印去什么地方，最短多久
    goTo(site,alt_time)

def goTo(site,atime):
    if site=='tour':
        onTour(atime)
    elif site=='home':
        inHome.inHome(atime)
    elif site=='school':
        inSchool(atime)
    return 0

if __name__ == '__main__':
    fun_timer()
