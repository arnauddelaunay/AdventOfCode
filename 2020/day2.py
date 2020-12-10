import re


def run1(input_path):
    inputs = list(map(lambda x: x.strip(), open(input_path).readlines()))
    pattern = r'^(\d*)-(\d*) (\w)\: (\w*)$'
    valid_password = 0
    for inp in inputs:
        matches = re.findall(pattern, inp)[0]
        minimum, maximum, letter, password = matches
        occurence_of_letter = password.count(letter)
        if (occurence_of_letter >= int(minimum)) & (occurence_of_letter <= int(maximum)):
            valid_password += 1
    return valid_password



def run2(input_path):
    inputs = list(map(lambda x: x.strip(), open(input_path).readlines()))
    pattern = r'^(\d*)-(\d*) (\w)\: (\w*)$'
    valid_password = 0
    for inp in inputs:
        matches = re.findall(pattern, inp)[0]
        pos1, pos2, letter, password = matches
        pos1_letter = password[int(pos1)-1]
        pos2_letter = password[int(pos2)-1]
        nb_good_positions = sum([(letter == pos1_letter), (letter == pos2_letter)])
        if nb_good_positions == 1:
            valid_password += 1
    return valid_password


if __name__ == '__main__':
    path = 'inputs/day2.txt'
    print(run1(path))
    print(run2(path))
