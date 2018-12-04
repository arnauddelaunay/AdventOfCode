# # DAY 11
import numpy as np

# In[40]:

def day_11(inp):
    moves = {
        's' : (2,0),
        'n' : (-2,0),
        'se' : (1, 1),
        'ne' : (-1,1),
        'sw' : (1,-1),
        'nw' : (-1,-1)
    }

    def add(pos, move):
        return (pos[0]+move[0], pos[1]+ move[1])

    def diff(pos, start):
        return (pos[0]-start[0], pos[1]-start[1])

    def compute_steps(pos):
        if abs(pos[1])>abs(pos[0]):
            s = abs(pos[1])
        else:
            s = abs(pos[1])+(abs(pos[0])-abs(pos[1]))/2
        return s

    pos = (0,0)
    steps = []
    poss = []
    for move in inp:
        pos = add(pos, moves[move])
        poss.append(pos)
        steps.append(compute_steps(pos))
    return (steps[-1], max(steps))
