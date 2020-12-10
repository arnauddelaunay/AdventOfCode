import re


def _parse(line):
    clean_line = line.strip()
    return clean_line


def run1(input_path):
    inputs = list(map(_parse, open(input_path).readlines()))
    nb_answers = []
    new_group = []
    for line in inputs:
        if line == '':
            nb_yes = len(set(new_group))
            nb_answers.append(nb_yes)
            new_group = []
            continue
        new_group += [c for c in line]
    nb_yes = len(set(new_group))
    nb_answers.append(nb_yes)
    return sum(nb_answers)


def run2(input_path):
    inputs = list(map(_parse, open(input_path).readlines()))
    group_size = 0
    nb_answers = []
    group_answers = {}
    for line in inputs:
        if line == '':
            nb_yes = len(list(filter(lambda item: item[1]==group_size, group_answers.items())))
            nb_answers.append(nb_yes)
            group_answers = {}
            group_size = 0
            continue
        for c in line:
            if c not in group_answers:
                group_answers[c] = 0
            group_answers[c] += 1
        group_size += 1
    nb_yes = len(list(filter(lambda item: item[1]==group_size, group_answers.items())))
    nb_answers.append(nb_yes)
    return sum(nb_answers)


if __name__ == '__main__':
    path = 'inputs/tests/day6.txt'
    #print(run1(path))
    #print(run2(path))
    
    path = 'inputs/day6.txt'
    print(run1(path))
    print(run2(path))

    