# # Day 13

import numpy as np

# In[103]:

def get_pos_of_scanner(rang, t):
    rest = np.mod(t,2*rang-2)
    return rest if rest<rang else np.mod(-rest+rang-1,rang-1)
    
def get_layers(inp):
    return map(lambda l : (int(l.split(': ')[0]), int(l.split(': ')[1])), inp)
    
def is_caught_on_layer(layer, delay=0):
    return (True, layer[0]*layer[1]) if get_pos_of_scanner(layer[1], layer[0]+delay)==0 else (False, 0)

def day_13_1(inp, delay=0):
    layers = get_layers(inp)
    return np.sum(map(lambda layer : is_caught_on_layer(layer, delay=delay)[1], layers))

def day_13_2(inp):
    layers = get_layers(inp)
    delay = 1
    while True:
        caught = False
        for layer in layers:
            caught = is_caught_on_layer(layer, delay=delay)[0]
            if caught:
                break
        if not caught:
            return delay
        delay+=1

day_13 = lambda inp : (day_10_1(inp), day_10_2(inp))
