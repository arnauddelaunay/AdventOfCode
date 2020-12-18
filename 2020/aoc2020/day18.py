import re

DAY = 18
OPERATORS = {
    '+': lambda a, b: a+b,
    '*': lambda a, b: a*b
}


def _to_string(elements, operators):
    nb_open_brackets = elements[0][1]
    s = '(' * nb_open_brackets
    for i, e in enumerate(elements[:-1]):
        s += str(e[0])
        n_brackets_to_close = nb_open_brackets - operators[i][1]
        s += '%s %s ' % (')' * n_brackets_to_close, operators[i][0])
        nb_open_brackets = operators[i][1]
    s += '%s%s' % (elements[-1][0], ')' * nb_open_brackets)
    return s


    



def _parse(line):
    clean_line = line.strip()
    elements_and_operators = re.findall(r'([()*+]|\d+)', clean_line)
    elements, operators = split_elements_and_operators(elements_and_operators)
    return elements, operators


def split_elements_and_operators(elements_and_operators):
    elements_level = []
    operators_level = []
    level = 0
    for element in elements_and_operators:
        if element == '(':
            level += 1
        elif element == ')':
            level -= 1
        else:
            if re.match(r'[+*]', element) is not None:
                operators_level.append((element, level))
            else:
                elements_level.append((element, level))
    return elements_level, operators_level


def add_prevalence(elements, operators):
    plus_operators_idx = [i for i, op in enumerate(operators) if operators[i][0] == '+']
    for i in plus_operators_idx:
        operator = operators[i]
        operator_level = operator[1]
        left_j = i
        while ((left_j-1) >= 0) and (operators[left_j-1][1] > operator_level):
            left_j -= 1
        left = elements[left_j:i+1]
        left_operators = operators[left_j:i]
        right_j = i
        while ((right_j+1) < len(operators)) and (operators[right_j+1][1] > operator_level):
            right_j += 1
        right = elements[i+1:right_j+2]
        right_operators = operators[i+1:right_j+1]
        elements = elements[:left_j] + _change_level(left, 1) + _change_level(right, 1) + elements[right_j+2:]
        operators = operators[:left_j] + _change_level(left_operators, 1) + _change_level([operator], 1) + _change_level(right_operators, 1) + operators[right_j+1:]
    return elements, operators


def _change_level(elements, sens=-1):
    return list(map(lambda x: (x[0], max(0, x[1]+sens*1)), elements))


def get_left_right(elements, operators):
    i = 0
    while min(map(lambda x: x[1], operators)) > 0:
        elements = _change_level(elements, -1) 
        operators = _change_level(operators, -1) 
    while operators[i][1] != 0:
        i+=1
    left = elements[:i+1]
    left_operators = operators[:i]
    j = i + 1
    while (j < len(operators)) and (operators[j][1] != 0):
        j += 1
    right = elements[i+1:j+1]
    right_operators = operators[i+1:j]
    next_operation_elements = elements[j+1:]
    next_operation_operators = operators[j:]
    return (
        _change_level(left, -1), _change_level(left_operators, -1), 
        operators[i][0], 
        _change_level(right, -1), _change_level(right_operators, -1),
        next_operation_elements, next_operation_operators
    )


def get_result(elements, operators):
    if len(operators) == 0:
        if len(elements) != 1:
            raise ValueError('parsing error')
        return int(elements[0][0])
    left_right_elements = get_left_right(elements, operators)
    (left, left_operators, operator, right, right_operators,
    next_operation_elements, next_operation_operators) = left_right_elements
    result = OPERATORS[operator](
        get_result(left, left_operators),
        get_result(right, right_operators)
    )
    return get_result([(result, 0)] + next_operation_elements, next_operation_operators)


def run1(input_path):
    lines = open(input_path).readlines()
    result_sum = 0
    for line in lines:
        elements, operators = _parse(line)
        result_sum += get_result(elements, operators)
    return result_sum


def run2(input_path):
    lines = open(input_path).readlines()
    result_sum = 0
    for line in lines:
        elements, operators = _parse(line)
        elements, operators = add_prevalence(elements, operators)
        res = get_result(elements, operators)
        result_sum += res
    return result_sum
    


if __name__ == '__main__':
    path = 'inputs/day%d.txt' % DAY
    print("Run 1", run1(path))
    print("Run 2", run2(path))
