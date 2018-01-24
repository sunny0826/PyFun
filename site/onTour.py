#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong
'''旅行'''
from logging.config import fileConfig
import logging
import gameMain

'''配置日志'''
fileConfig('./log/logging.conf')
logger=logging.getLogger('infoLogger')

def onTour(time):
    gameMain.fun_timer()