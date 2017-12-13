# # Day 2
import numpy as np
# In[64]:

def day_2_1(inp):
    return int(np.array(map(lambda x : x.max() - x.min(), inp)).sum())

def day_2_2(inp):
    def get_div(row):
        for i, e in enumerate(row):
            for e2 in np.hstack((row[:i],row[i+1:])):
                if e%e2==0:
                    return e/e2
    return int(np.array(map(get_div, inp)).sum())

day_2 = lambda inp : (day_2_1(inp),day_2_2(inp))
