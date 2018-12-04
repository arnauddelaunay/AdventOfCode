# # Day 1
import numpy as np

# In[62]:

def get_output(inp, i, add):
    return int(inp[i]) if inp[i]==inp[np.mod(i+add,len(inp))] else 0

def day_1(inp):
    S1 = 0
    S2 = 0
    for i in range(len(inp)):
        S1+=get_output(inp,i,1)
        S2+=get_output(inp,i,len(inp)/2)
    print S1,S2