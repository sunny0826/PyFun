#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong
import time

def welcome():
    f = open('../txtResource/welcome.txt', 'r')
    print(f.read())
    user_name = input("who are you:")
    for i in range(101):
        string = 'loading... ' + str(i) + '%'
        # print(string,end='')    # 不换行
        # print('\b' * len(string),end='', flush=True)    # 删除前面打印的字符
        time.sleep(0.1)

    return user_name

# if __name__ == '__main__':
#     welcome()