#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong
'''用于计算概率'''
# 以指定的概率获取元素 以一个列表为基准概率，从一个列表中随机获取元素
import random

def random_pick(some_list, probabilities):
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for item, item_probability in zip(some_list, probabilities):
        cumulative_probability += item_probability
        if x < cumulative_probability: break
    return item


# event_list = ['home', 'school', 'tour']
# probabilities = [0.2, 0.2, 0.6]
# print(random_pick(event_list, probabilities))
# 根据权重来获取 核心在于权重乘以 就相当于次数
# def random_pick_odd(some_list, odds):
#     print('权重乘积')
#     table = [z for x, y in zip(some_list, odds) for z in [x] * y]
#     print(table)
#     return random.choice(table)
# some_list = [1, 2, 3, 4]
# odds = [3, 1, 4, 2]
# print(random_pick_odd(some_list, odds))
