# # DAY 8

# In[21]:

import operator
import numpy as np

def day_8(inp):
    ACTIONS = {'inc' : 1, 'dec' : -1}
    CONDITIONS = {"==" : lambda x,y : x==y,
                  "!=" : lambda x,y : x!=y,
                  "<=" : lambda x,y : x<=y,
                  ">=" : lambda x,y : x>=y,
                  ">" : lambda x,y : x>y,
                  "<" : lambda x,y : x<y
                 }
    variables = {'max_value' : -np.inf}
    
    def code_parser(line):
        """
        <inp_variable> <action> <var_value> if <cond_variable> <condition> <cond_value>
        """
        inp_variable, action, var_value, _, cond_variable, condition, cond_value = line.split()
        variables[inp_variable] = 0 if inp_variable not in variables else variables[inp_variable]
        variables[cond_variable] = 0 if cond_variable not in variables else variables[cond_variable]
        if CONDITIONS[condition](variables[cond_variable], int(cond_value)):
            variables[inp_variable] = variables[inp_variable] + ACTIONS[action]*int(var_value)
            variables['max_value'] = max(variables['max_value'], variables[inp_variable])

    map(code_parser, inp)
    max_value = variables['max_value']
    del variables['max_value']
    return(max(variables.itervalues()), max_value)
