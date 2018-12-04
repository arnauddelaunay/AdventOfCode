# # DAY 10
import numpy as np

# In[35]:

# DAY 10.1
def modify_list(L, current_position, length, skip_size):
    N = (current_position+length)
    number_of_first_elements = max(0,N-len(L))
    sub_list = L[current_position:N] + L[:number_of_first_elements]
    sub_list.reverse()
    L[current_position:N] = sub_list[:(length-number_of_first_elements)]
    L[:number_of_first_elements] = sub_list[length-number_of_first_elements:]
    return L, np.mod((current_position+length+skip_size),len(L)), skip_size+1

def day_10_1(inp):
    L = range(256)
    current_position = 0
    skip_size = 0
    for length in inp:
        L, current_position, skip_size = modify_list(L, current_position, length, skip_size)
    return L[0]*L[1]


# In[38]:

inp = get_inp('10')[:-1]

def to_ascii(string):
    return [ord(c) for c in string]

def get_lengths(string):
    return to_ascii(string)+[17, 31, 73, 47, 23]

def get_sparse_hash(string):
    L = range(256)
    current_position = 0
    skip_size = 0
    lengths = get_lengths(string)
    for length in lengths*64:
        L, current_position, skip_size = modify_list(L, current_position, length, skip_size)
    return L

def perform_xor(list_of_nums):
    S = 0
    for x in list_of_nums:
        S ^= x
    return S

def to_dense(sparse):
    return ''.join(
        map(
            lambda x : hex(x)[2:] if len(hex(x)[2:])==2 else '0%s' % hex(x)[2:],
            map(
                lambda sixteens : perform_xor(sixteens),
                [sparse[16*i:16*(i+1)] for i in range(16)]
            )
        ))

def day_10_2(inp):
    inp = ','.join(map(str,inp))
    return to_dense(get_sparse_hash(inp))

day_10 = lambda inp : (day_10_1(inp), day_10_2(inp))
