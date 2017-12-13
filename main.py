
# coding: utf-8

# # AdventOfCode 2017
# 
# #### Arnaud Delaunay

import sys
import ConfigParser

from days import *

if __name__ == '__main__':


    add_day_func_to_dict(day_1, '1', mode=0)
    add_day_func_to_dict(day_2, '2', mode='np')
    add_day_func_to_dict(day_3, '3', mode='np')
    add_day_func_to_dict(day_4, '4', mode=0, callback=lambda x : x.split('\n'))
    add_day_func_to_dict(day_5, '5')
    add_day_func_to_dict(day_6, '6', mode='np', callback=lambda x : x.astype(int))
    add_day_func_to_dict(day_7, '7', mode=0, callback=lambda x : x.split('\n'))
    add_day_func_to_dict(day_8, '8', mode=0, callback=lambda x : x.split('\n'))
    add_day_func_to_dict(day_9, '9', mode=0)
    add_day_func_to_dict(day_10, '10', mode=0, callback=lambda x : map(int, x.split(',')))
    add_day_func_to_dict(day_11, '11', mode=0, callback=lambda x : x.split(','))
    add_day_func_to_dict(day_12, '12', mode=0, callback=lambda x : x.split('\n'))
    add_day_func_to_dict(day_13, '13', mode=0, callback=lambda x : x.split('\n')[:-1])
