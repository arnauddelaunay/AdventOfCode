import numpy as np

DAY = 15


def _parse(line):
    clean_line = line.strip()
    return list(map(int, clean_line.split(',')))


def get_spoken_number(starting_numbers, n):
    memory = dict([(v, {'last_time_spoken': i+1, 'spoken': 1}) for i, v in enumerate(starting_numbers)])
    last_spoken_number = starting_numbers[-1]
    serie = starting_numbers
    for i in range(len(starting_numbers) + 1, n+1):
        # new turn
        if memory[last_spoken_number]['spoken'] > 1:
            previously_spoken = last_spoken_number
            last_spoken_number = i - 1 - memory[last_spoken_number]['last_time_spoken']
            memory[previously_spoken]['last_time_spoken'] = i - 1
        else:
            last_spoken_number = 0
        # register last spoken in memomry
        if last_spoken_number not in memory:
            memory[last_spoken_number] = {'last_time_spoken': i, 'spoken': 1}
        else:
            memory[last_spoken_number]['spoken'] += 1
        serie = serie[1:] + [last_spoken_number]
        if serie == starting_numbers:
            print("finding a loop at turn %d" % i)
            break
    if i != n:
        idx = n%i
        last_spoken_number = [k for k, v in memory.items() if v['last_time_spoken'] == idx][0]
    return last_spoken_number
    

def run1(input_path):
    starting_numbers = _parse(open(input_path).readlines()[0])
    return get_spoken_number(starting_numbers, 2020)


def run2(input_path):
    starting_numbers = _parse(open(input_path).readlines()[0])
    return get_spoken_number(starting_numbers, 30000000)


if __name__ == '__main__':
    path = 'inputs/day%d.txt' % DAY
    print("Run 1", run1(path))
    print("Run 2", run2(path))
