# # Day 3
import numpy as np

# In[74]:

#DAY 3.1
def get_path_to_1(inp):
    k = int(np.sqrt(inp))
    K = k/2 - (1-k%2)
    I = k%2
    p = inp-(k*k)
    return abs(K-min(p-1, k))+abs(K+I-max(p-k-1,0))

# %time get_path_to_1(inp)

#DAY 3.2

#USELESS FINALLY
def get_coordinates(inp):
    if inp == 1:
        return 0,0
    k = int(np.sqrt(inp))
    K = k/2
    p = inp-(k*k)
    add = 1 if p==0 else 0 # if it's a square
    I = (-1)**(k%2+1)*(K-min(p-1,k)-add)
    J = (-1)**(k%2+1)*(K+k%2-max(p-k-1,0)-add)
    return I, J

def get_idx(I,J):
    if (I,J) == (0,0):
        return 1
    sign = np.sign(J-I) if J!=I else -1 #we want sign(0)=-1
    K = max(sign*J, -sign*I)-1
    k = K*2+1-min(0,sign)
    N = K +k**2+1
    N += -sign*I - 1*(min(sign, 0)) if -sign*I<=sign*J else -sign*J + k + 1
    return int(N)

M = {}
def compute_sum(I,J):
    if I==0 and J==0:
        return 1
    if '%d,%d' % (I,J) in M:
        return M['%d,%d' % (I,J)]
    this_idx = get_idx(I,J)
    S = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if get_idx(I+i,J+j)<this_idx:
                if '%d,%d' % (I+i,J+j) not in M:
                    M['%d,%d' % (I+i,J+j)] = compute_sum(I+i,J+j)
                S+=M['%d,%d' % (I+i,J+j)]
    return S

def find_smallest_larger_than(X):
    k = 0
    while(True):
        if compute_sum(k,k)>X:
            sign=1
            if compute_sum(-k,-k)<X:
                sign = -1 
            value = compute_sum(sign*(k-1),sign*k)
            s = 2
            while X>value:
                value = compute_sum(sign*(k-min(s,2*k)),sign*(k-max(s-2*k,0)))
                s+=1
            return value
        k += 1
        
# %time find_smallest_larger_than(10211726171726281982716820)

day_3  = lambda inp : (get_path_to_1(inp), find_smallest_larger_than(inp))