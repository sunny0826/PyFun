#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong
import threading
import time
from timer import in_time_range

def fun_timer():
    time_now = time.strftime('%H:%M:%S', time.localtime(time.time()))
    if in_time_range("00:00:00-02:59:59"):
        print("foredawn")
    elif in_time_range("03:00:00-05:59:59"):
        print("dawn")
    elif in_time_range("06:00:00-08:59:59"):
        print("morning")
    elif in_time_range("09:00:00-11:59:59"):
        print("forenoon")
    elif in_time_range("12:00:00-14:59:59"):
        print("noon")
    elif in_time_range("15:00:00-17:59:59"):
        print("afternoon")
    elif in_time_range("18:00:00-20:59:59"):
        print("dusk")
    elif in_time_range("21:00:00-23:59:59"):
        print("midnight")
    else:
        print("F")
    print(time_now)
    global timer
    timer = threading.Timer(5, fun_timer)
    timer.start()


timer = threading.Timer(1, fun_timer)
timer.start()

