#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong
import time

for i in range(101):
    string = 'loading... ' + str(i) + '%'
    print(string, end='')    # 不换行
    print('\b' * len(string), end='', flush=True)    # 删除前面打印的字符
    time.sleep(0.2)
