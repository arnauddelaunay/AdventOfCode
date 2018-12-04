import sys
sys.setrecursionlimit(100000)
import numpy as np

def get_inp(day, mode='np'):
    if mode=='np':
        try:
            return np.loadtxt('inputs/day%s' % day)
        except:
            return open('inputs/day%s' % day).read()[:-1]
    return open('inputs/day%s' % day).read()[:-1]
        

outputs = {}

def reload_answers(day):
    outputs[day]['answers'] = outputs[day]['func'](day)
    return outputs[day]['answers']

def add_day_func_to_dict(day_func, day, mode='np', callback=None):
    inp = get_inp(day, mode=mode)
    if callback:
        inp = callback(inp)
    f = lambda day : day_func(inp)
    outputs[day] = {
        'func' : f,
        'answers' : f(day)
    }
    return outputs[day]['answers']

from parsy import regex, string, seq
command = regex('[a-z]{3}')
space = string(" ")
var = regex('[a-z]{1}')
value = (regex('[-+]?\d+').map(int) | var).optional()
action = seq(command, space >> value, space.optional() >> value)
action.parse('hed a -13')

inp_test = ['snd 1','snd 2','snd p','rcv a','rcv b','rcv c','rcv d']
inp = get_inp('18').split('\n')
import socket

def create_socket(p):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host = socket.gethostname()
    port = 9995+p
    serversocket.bind((host, port))                                  
    serversocket.listen(100)
    return serversocket

def send_to_socket(value, p):
    new_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    new_sock.connect((socket.gethostname(),9995+p))
    new_sock.send(str(value).encode('ascii'))
    new_sock.close()
    
def get_value_from_socket_queue(p, sockets):
    clientsocket, addr = sockets[p].accept()
    value = int(clientsocket.recv(1024).decode('ascii'))
    clientsocket.close()
    return value                    
            
variables = {
    0 : {
        'p' : 0
    },
    1 : {
        'p' : 1,
        'send' : 0
    }
}

def check(var, p=0):
    if var not in variables[p]:
        variables[p][var] = 0
    
def get_value(value, p=0):
    if type(value)==int:
        return value
    else:
        check(value, p=p)
        return variables[p][value]
    
def snd(var, value, p=0):
    v = get_value(var, p=p)
    if p==1:
        variables[p]['send']+=1
        with open('out.txt', 'w') as out:
            out.write('%d\n' % variables[p]['send'])
    send_to_socket(v, (1-p))
    return 1, None
    
def set_(var, value, p=0):
    variables[p][var] = get_value(value, p=p)
    return 1, None
    
def add(var, value, p=0):
    check(var, p=p)
    variables[p][var] += get_value(value, p=p)
    return 1, None
    
def mul(var, value, p=0):
    check(var, p=p)
    variables[p][var] *= get_value(value, p=p)
    return 1, None
    
def mod(var, value, p=0):
    check(var, p=p)
    variables[p][var] %= get_value(value, p=p)
    return 1, None

def rcv(var, value, p=0):
    value = get_value_from_socket_queue(p, sockets)
    variables[p][var] = value
    return 1, None
    
def jgz(var, value, p=0):
    next_step=1
    check(var, p=p)
    if variables[p][var]>0:
        next_step = get_value(value, p=p)
    return next_step, None

mapper = {
    'snd' : snd,
    'set' : set_,
    'add' : add,
    'mul' : mul,
    'mod' : mod,
    'rcv' : rcv,
    'jgz' : jgz
}
def apply_func(inp, idx, p):
    parsed = action.parse(inp[idx])
    return mapper[parsed[0]](parsed[1], parsed[2], p=p)

sockets = [create_socket(p) for p in range(2)]


import threading
import time


class ThreadingWorker(object):

    def __init__(self, actions, p=0):
        self.p = p
        self.actions = actions

        self.thread = threading.Thread(target=self.run, args=())
        self.thread.daemon = True                            # Daemonize thread
        self.thread.start()                                  # Start the execution

    def run(self):
        idx = 0
        while True:
            step, value = apply_func(self.actions, idx, self.p)
            idx += step

thread0 = ThreadingWorker(inp, p=0)
thread1 = ThreadingWorker(inp, p=1)
