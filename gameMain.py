#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong
import logging
from logging.config import fileConfig

from control.proBability import random_pick

from sitewhere import inHome
from sitewhere import inSchool
from sitewhere import onTour
from welcome import welcome

'''配置日志'''
fileConfig('./log/logging.conf')
logger=logging.getLogger('infoLogger')

def fun_timer():
    #配置概率
    event_list = ['home', 'school', 'tour']
    probabilities = [0, 0, 1]
    site = random_pick(event_list, probabilities)
    alt_list = [16, 8, 10, 12, 24]
    probabilities = [0.1, 0.3, 0.5, 0.1]
    alt_time = random_pick(alt_list, probabilities)
    logging.warning('SITE:'+site+',AT LEAST:'+str(alt_time)+'h')#打印去什么地方，最短多久
    goTo(site,alt_time)

def goTo(site,atime):
    if site=='tour':
        onTour.doTour(atime)
    elif site=='home':
        inHome.doHome(atime)
    elif site=='school':
        inSchool.doSchool(atime)
    return 0

if __name__ == '__main__':
    user_name = welcome.welcome()
    fun_timer()
