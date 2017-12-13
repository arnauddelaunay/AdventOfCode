# # DAY 12
import numpy as np

# In[42]:

def parser(line, neighbors):
    idx, neighs = line.split(' <-> ')
    idx = int(idx)
    neighs = map(int, neighs.split(','))
    if idx not in neighbors:
        neighbors[idx] = set()
    map(lambda n : neighbors[idx].add(n), neighs)
    return neighs, neighbors

def get_all_neighs_of_idx(inp, idx, neighbors):
    all_neighs = set([idx])
    direct_neighs, neighbors = parser(inp[idx], neighbors)
    map(lambda n : all_neighs.add(n), direct_neighs)
    for new_id in direct_neighs:
        if new_id not in neighbors:
            this_neighs, neighbors = get_all_neighs_of_idx(inp, new_id, neighbors)
            map(lambda n : all_neighs.add(n), this_neighs)
    return all_neighs, neighbors

def get_all_groups(inp):
    neighbors = {}
    groups = []
    ids_in_groups = set()
    for idx in range(len(inp)):
        if idx not in ids_in_groups:
            new_group, neighbors = get_all_neighs_of_idx(inp, idx, neighbors)
            ids_in_groups = ids_in_groups.union(new_group)
            groups.append(new_group)
    return groups

""" TESTS
test = ["0 <-> 2", "1 <-> 1","2 <-> 0, 3, 4","3 <-> 2, 4","4 <-> 2, 3, 6","5 <-> 6","6 <-> 4, 5"]group_test, _ = get_all_neighs_of_idx(test, 0, {})
groups = get_all_groups(test)
groups
"""

def day_12(inp):
    group_real, _ = get_all_neighs_of_idx(inp, 0, {})
    groups = get_all_groups(inp)
    return (len(group_real), len(groups))
