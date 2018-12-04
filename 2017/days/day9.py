# # DAY 9
import numpy as np
import re

# In[26]:

def remove_char(inp):
    return re.sub('!.{1}', '', inp)

def remove_garbage(inp):
    return re.sub('<.*?>', '', inp)

def count_in_garbage(inp):
    myre = re.compile(r'<.*?>')
    return np.sum(len(x) for x in map(lambda x : x[1:-1], myre.findall(inp)))

def get_subgroups(inp):
    return inp[1:-1].split(',')

def parenthetic_contents(string):
    stack = []
    for i, c in enumerate(string):
        if c == '{':
            stack.append(i)
        elif c == '}' and stack:
            start = stack.pop()
            yield (len(stack), string[start + 1: i])
            
day_9_1 = lambda inp : np.sum([depth+1 for depth, val in parenthetic_contents(remove_garbage(remove_char(inp)))])
day_9_2 = lambda inp : count_in_garbage(remove_char(inp))

day_9 = lambda inp : (day_9_1(inp), day_9_2(inp))
