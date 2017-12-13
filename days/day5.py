# # DAY 5
import numpy as np

# In[98]:

def get_number_of_steps(this_inp, change, change2_if_condition=1, condition=3):
    inp = this_inp.copy()
    cursor = 0
    L = len(inp)
    step = 0
    while True:
        prev = cursor
        cursor += inp[cursor]
        inp[prev] += change2_if_condition if inp[prev]>=condition else change
        step +=1
        if cursor >= L or cursor <0:
            break
    return step

day_5 = lambda inp : (get_number_of_steps(inp, 1), get_number_of_steps(inp, 1, -1, 3))

