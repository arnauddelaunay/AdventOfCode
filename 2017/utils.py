import sys
sys.setrecursionlimit(100000)
import numpy as np

def get_inp(day, mode='np'):
    if mode=='np':
        try:
            return np.loadtxt('inputs/day%s' % day)
        except:
            return open('inputs/day%s' % day).read()[:-1]
    return open('inputs/day%s' % day).read()[:-1]
        

outputs = {}

def reload_answers(day):
    outputs[day]['answers'] = outputs[day]['func'](day)
    return outputs[day]['answers']

def add_day_func_to_dict(day_func, day, mode='np', callback=None):
    inp = get_inp(day, mode=mode)
    if callback:
        inp = callback(inp)
    f = lambda day : day_func(inp)
    outputs[day] = {
        'func' : f,
        'answers' : f(day)
    }
    return outputs[day]['answers']