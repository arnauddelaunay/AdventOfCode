# # DAY 6

# In[19]:

import multiprocessing
from functools import partial
import numpy as np

def day_6(inp):
    L=len(inp)
    states =[] 

    def choose_bank(inp):
        return inp.argmax()

    def get_spread(idxn_b, iv):
        i, v = iv
        idx, n_b = idxn_b
        # print i, v, idx, n_b
        if i == idx:
            v = 0
        S=v+n_b/L
        if np.mod((i-idx)-1, L)<(n_b%L):
            S+=1
        return S

    def spread_blocks(idx, inp):
        n_b = inp[idx] 
        #pool = multiprocessing.Pool()
        #inp = pool.map(partial(get_spread, (idx,n_b)), enumerate(inp))
        inp = map(partial(get_spread, (idx,n_b)), enumerate(inp))
        return np.array(inp) 

    step = 0
    while True:
        idx = choose_bank(inp) 
        inp = spread_blocks(idx, inp)
        hashinp = hash(inp.tostring())
        step += 1
        if hashinp in states:
            break
        states.append(hashinp)

    return (step, len(states)-states.index(hashinp))
