#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong
'''旅行'''
import threading
from logging.config import fileConfig
import logging
import gameMain
from control.proBability import random_pick_odd
from control.py_mail import send_html

'''配置日志'''
fileConfig('./log/logging.conf')
logger=logging.getLogger('infoLogger')

def onTour(itime):
    events = event()
    when = itime - 2
    timer = threading.Timer(2 * 300, onTour, [when])
    logging.info('go to '+events+', remaining ' + str(when) + 'h')
    if when < 0:
        timer.cancel()
        gameMain.fun_timer()
    where = ''
    if events=='爱知县':
        where = 'mingguwu'
        site_name = '名古屋城'
    elif events=='兵库县':
        where = 'youmawenquan'
        site_name = '有马温泉'
    elif events == '大分县':
        where = 'biefuwenquan'
        site_name = '别府温泉'
    elif events == '京都市':
        site_list = ['tianqiaoli','yuzhiqiao']
        odds = [1,1]
        where = random_pick_odd(site_list, odds)
        if where == 'tianqiaoli':
            site_name = '天桥立'
        elif where == 'yuzhiqiao':
            site_name= '宇治桥'
    elif events == '鹿儿岛':
        where = 'shengwenshan'
        site_name = '绳文杉'
    elif events == '青森县':
        where = 'aorulaixiliu'
        site_name = '奥入濑溪流'
    elif events == '秋田县':
        where = 'rudaoqidengta'
        site_name = '入道埼灯塔'
    elif events == '群马县':
        where = 'caojinwenquan'
        site_name = '草津温泉'
    elif events == '长野县':
        where = 'xinzhoushanguangsi'
        site_name = '信州善光寺'
    else:
        raise ValueError('地点参数有误，请重新输入')
    send_html('Tour', where, '旅行到了 '+events+' 的 '+site_name+' 好开心！')
    timer.start()


'''
爱知 名古屋城：mingguwu
兵库 有马温泉：youmawenquan
大分 别府温泉：biefuwenquan
京都 天桥立：tianqiaoli
京都 宇治桥：yuzhiqiao
鹿儿岛 绳文杉：shengwenshan
青森 奥入濑溪流：aorulaixiliu
秋田 入道埼灯塔：rudaoqidengta
群马 草津温泉：caojinwenquan
长野 信州善光寺：xinzhoushanguangsi
'''
'''概率调整'''
def event():
    logging.debug('说走就走的旅行！')
    site_list = ['爱知县', '兵库县', '大分县', '京都市', '鹿儿岛','青森县','秋田县','群马县','长野县']
    odds = [1,1,1,1,1,1,1,1,1]
    events = random_pick_odd(site_list, odds)
    return events