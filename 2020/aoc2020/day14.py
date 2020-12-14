import re

DAY = 14

def _parse(line):
    clean_line = line.strip()
    pattern = r'^(mask|mem\[(\d+)\]) = (\w+)$'
    matches = re.findall(pattern, clean_line)[0]
    if matches[0] == 'mask':
        return ('mask', matches[2])
    else:
        return (int(matches[1]), int(matches[2]))


def int2bin(i):
    return bin(i).split('b')[-1]


def run1(input_path):
    mask = ''
    memory = {}
    for instruction, value in map(_parse, open(input_path).readlines()):
        if instruction == 'mask':
            mask = value
        else:
            value = int2bin(value)
            new_value = ['0']*(36-len(value)) + [c for c in value]
            for i, bit in enumerate(mask):
                if bit != 'X':
                    new_value[i] = bit
            memory[instruction] = int(''.join(new_value), 2)
    return sum(memory.values())


def run2(input_path):
    mask = ''
    memory = {}
    for instruction, value in map(_parse, open(input_path).readlines()):
        if instruction == 'mask':
            mask = value
        else:
            instruction = int2bin(instruction)
            potential_adresses = [['0']*(36-len(instruction)) + [c for c in instruction]]
            for i, bit in enumerate(mask):
                if bit == '1':
                    for add in potential_adresses:
                        add[i] = bit
                if bit == 'X':
                    new_potential_adresses = []
                    for add in potential_adresses:
                        add[i] = '0'
                        new_potential_adresses.append(add[:i] + ['1'] + add[i+1:])
                    potential_adresses += new_potential_adresses
            for address in potential_adresses:
                memory_address = int(''.join(address), 2)
                memory[memory_address] = value
    return sum(memory.values())
    



if __name__ == '__main__':
    path = 'inputs/day%d.txt' % DAY
    print("Run 1", run1(path))
    print("Run 2", run2(path))
