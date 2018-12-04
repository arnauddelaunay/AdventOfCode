# # DAY 4
import numpy as np

# In[81]:

def check_passphrase(paph):
    L = paph.split(' ')
    return len(L)==len(set(L))
def day_4_1(inp):
    return sum(map(check_passphrase,inp))

#inp = get_inp('4').split('\n')[:-1]
#day_4_1(inp)

def doublecheck_passphrase(paph):
    L = map(lambda x : set(x), paph.split(' '))
    unique = reduce(lambda l, x: l.append(x) or l if x not in l else l, L, [])
    return len(unique)==len(L)

def day_4_2(inp):
    return sum(map(doublecheck_passphrase,inp))

#inp = get_inp('4').split('\n')[:-1]
#day_4_2(inp)

day_4 = lambda inp : (day_4_1(inp), day_4_2(inp))
