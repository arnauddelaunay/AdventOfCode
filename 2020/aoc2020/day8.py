import re


def _parse(line):
    clean_line = line.strip()
    pattern = r'(nop|acc|jmp) ([+-]\d+)'
    action, value = re.findall(pattern, clean_line)[0]
    return action, value


def run_loop(inputs):
    accumulator = 0
    visited = []
    cursor = 0
    while True:
        if cursor in visited:
            loop = True
            break
        if cursor >= len(inputs):
            loop = False
            break
        action, value = inputs[cursor]
        visited.append(cursor)
        if action == 'acc':
            accumulator += int(value)
        cursor_change = 1
        if action == 'jmp':
            cursor_change = int(value)
        cursor += cursor_change
    return loop, accumulator


def run1(input_path):
    inputs = list(map(_parse, open(input_path).readlines()))
    _, accumulator = run_loop(inputs)
    return accumulator


def run2(input_path):
    inputs = list(map(_parse, open(input_path).readlines()))
    for i, inp in enumerate(inputs):
        if inp[0] == 'jmp':
            new_action = 'nop'
        elif inp[0] == 'nop':
            new_action = 'jmp'
        else:
            new_action = 'acc'
        new_inputs = inputs[:i] + [(new_action, inp[1])] + inputs[i+1:]
        loop, accumulator = run_loop(new_inputs)
        if not loop:
            print("Changing %dth line with %s works !" % (i, new_action))
            break
    return accumulator


if __name__ == '__main__':
    path = 'inputs/day8.txt'
    print(run1(path))
    print(run2(path))

    