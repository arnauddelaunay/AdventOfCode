import re
import copy

DAY = 16


def parse(lines):
    i = 0
    rules = {}
    while lines[i] != '\n':
        field, range_nbs = _parse(lines[i])
        rules[field] = range_nbs
        i += 1
    i += 2
    my_ticket = _parse(lines[i])
    i += 3
    other_tickets = [_parse(lines[k]) for k in range(i, len(lines))]
    return rules, my_ticket, other_tickets


def _parse(line):
    clean_line = line.strip()
    rule_pattern = r'([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)'
    matches = re.findall(rule_pattern, clean_line)
    if len(matches) > 0:
        field, i1, i2, i3, i4 = matches[0]
        return field, list(range(int(i1), int(i2)+1)) + list(range(int(i3), int(i4)+1))
    else:
        return list(map(int, clean_line.split(',')))


def filter_valid_tickets(rules, tickets):
    invalid_sum = 0
    ranges = []
    for rule_range in rules.values():
        ranges += rule_range
    invalid_tickets = []
    for i, values in enumerate(tickets):
        for value in values:
            if value not in ranges:
                invalid_sum += value
                invalid_tickets.append(i)
    valid_tickets = [tickets[i] for i in range(len(tickets)) if i not in invalid_tickets]
    return invalid_sum, valid_tickets
    

def run1(input_path):
    lines = open(input_path).readlines()
    rules, _, other_tickets = parse(lines)
    invalid_sum, _ = filter_valid_tickets(rules, other_tickets)
    return invalid_sum


def run2(input_path):
    lines = open(input_path).readlines()
    rules, my_ticket, other_tickets = parse(lines)
    _, valid_tickets = filter_valid_tickets(rules, other_tickets)
    available_positions = list(range(len(my_ticket)))
    rules_positions = []
    for rule, rule_range in rules.items():
        possible_positions = copy.copy(available_positions)
        for ticket in valid_tickets + [my_ticket]:
            for i in possible_positions:
                v = ticket[i]
                if v not in rule_range:
                    possible_positions.remove(i)
        if len(possible_positions) == 1:
            available_positions.remove(possible_positions[0])
        rules_positions.append(possible_positions)
    while len(available_positions) > 0:
        new_positions = []
        for rp in rules_positions:
            if len(rp) > 1:
                rp = list(filter(lambda p: p in available_positions, rp))
                if len(rp) == 1:
                    available_positions.remove(rp[0])
            new_positions.append(rp)
        rules_positions = new_positions
    keyword = 'departure'
    result = 1
    for i, rule in enumerate(rules.keys()):
        if rule[:len(keyword)] == keyword:
            result *= my_ticket[rules_positions[i][0]]
    return result


if __name__ == '__main__':
    path = 'inputs/day%d.txt' % DAY
    print("Run 1", run1(path))
    print("Run 2", run2(path))
