import numpy as np

DAY = 13


def _parse(line):
    clean_line = line.strip()
    if ',' not in clean_line:
        return int(clean_line)
    else:
        bus_ids = clean_line.split(',')
        buses = {}
        for i, b_id in enumerate(bus_ids):
            if b_id != 'x':
                buses[int(b_id)] = i
        return buses


def get_first_timestamp(buses):
    bus_ids_offsets = list(buses.items())
    bus0 = bus_ids_offsets[0][0]
    timestamp = 0
    step = 1
    i = 1
    multiplier = 0
    while i < len(bus_ids_offsets):
        bus_id, bus_offset = bus_ids_offsets[i]
        while ((timestamp + bus_offset) % bus_id) != 0:
            multiplier += step
            timestamp = bus0*multiplier
        step = step*bus_id
        i += 1
    return timestamp


def run1(input_path):
    time, buses = list(map(_parse, open(input_path).readlines()))
    bus_id, min_waiting_time = (0, np.inf)
    for b in buses.keys():
        bus_waiting_time = b - (time % b)
        if bus_waiting_time < min_waiting_time:
            min_waiting_time = bus_waiting_time
            bus_id = b
    return bus_id * min_waiting_time


def run2(input_path):
    _, buses = list(map(_parse, open(input_path).readlines()))
    return get_first_timestamp(buses)


if __name__ == '__main__':
    path = 'inputs/day%d.txt' % DAY
    print("Run 1", run1(path))
    print("Run 2", run2(path))
