# # DAY 7
import numpy as np
# In[14]:

def get_root(inp):
    inp = map(lambda x : x.split(' '), inp)
    leafs = dict([(l[0], {'w' : int(l[1].replace('(','').replace(')',''))}) for l in inp if '->' not in l])
    roots = dict([
        (l[0], {
                'w' : int(l[1].replace('(','').replace(')','')),
                'sons' : map(lambda x : x.replace(',',''), l[l.index('->')+1:])
               }) for l in inp if '->' in l])
    leafs_of_roots = [leaf for word in roots for leaf in roots[word]['sons']]
    for root in roots:
        if root not in leafs_of_roots:
            return root, roots, leafs

answer_7_1 = lambda inp : get_root(inp)[0]

def get_weights_of_sons(word, leafs, roots):
    if word in leafs:
        return leafs[word]['w']
    else:
        return np.sum([get_weights_of_sons(w, leafs, roots) for w in roots[word]['sons']]) + roots[word]['w']

def get_unbalanced_son(word, leafs, roots):
    if word in leafs:
        return None, None, None
    L = [get_weights_of_sons(w, leafs, roots) for w in roots[word]['sons']]
    value = len(set(L))==1
    if value:
        return None, None, None
    else:
        for i, l in enumerate(L):
            if L.count(l)==1:
                return roots[word]['sons'][i], l, L[np.mod((i+1),len(L))]

def answer_7_2(inp):
    word, roots, leafs = get_root(inp)
    should_be = 0
    v = 0
    while word is not None:
        prev_word, diff = (word, v-should_be)
        word, should_be, v = get_unbalanced_son(word, leafs, roots)
    #print "Bad value is %d, should be %d (weight of word %s)" % (roots[prev_word]['w'], roots[prev_word]['w'] + diff, prev_word)
    return roots[prev_word]['w'] + diff

day_7 = lambda inp : (answer_7_1(inp), answer_7_2(inp))