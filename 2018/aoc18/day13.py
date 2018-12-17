import numpy as np
import os
from termcolor import colored
import time

from .aoc import AOCDay


straight = np.array([
    [1, 0],
    [0, 1]])

left = np.array([
    [ 0, 1],
    [-1, 0]])

right = np.array([
    [0, -1],
    [1,  0]])

anti_slash = np.array([
    [0, 1],
    [1, 0]])

slash = np.array([
    [ 0, -1],
    [-1,  0]])


def build_action(move_array):
    return np.vstack([
        np.hstack([np.identity(2), np.zeros((2,2))]),
        np.hstack([move_array]*2)
    ])


milestone_mapping = {
    "-": build_action(straight),
    "|": build_action(straight),
    "\\": build_action(anti_slash),
    "/": build_action(slash),
    ">": build_action(straight),
    "<": build_action(straight),
    "^": build_action(straight),
    "v": build_action(straight),
    "+": "intersection"
}

carts_mapping = {
    ">": np.array([ 0,  1]),
    "<": np.array([ 0, -1]),
    "v": np.array([ 1,  0]),
    "^": np.array([-1,  0])
}

inv_carts_mapping = dict([("".join(map(str, v)), k) for k, v in carts_mapping.items()])

colors = ["red", "blue", "green", "yellow", "white", "magenta", "cyan", "grey"]

intersections = [build_action(left), build_action(straight), build_action(right)]


class Milestone:

    def __init__(self, string):
        self.string = string
        self.action = milestone_mapping[string]

    def __str__(self):
        return self.string

    def __repr__(self):
        return "Milestone(%s)" % self.string


def get_collisions(carts_map):
    collisions = []
    for i in range(len(carts_map) - 1):
        for j in range(i + 1, len(carts_map)):
            if np.array_equal(carts_map[i]["cart"][:2], carts_map[j]["cart"][:2]):
                # if np.array_equal(carts_map[i]["cart"][2:], -carts_map[j]["cart"][2:]):
                collisions.append((i, j))
    return collisions


def check_collisions(cart_id, carts_map):
    for other_id in [i for i in carts_map.keys() if i != cart_id]:
        if np.array_equal(carts_map[cart_id]["cart"][:2], carts_map[other_id]["cart"][:2]):
            return True, (cart_id, other_id)
    return False, None


def sort_carts(carts_map):
    return sorted(carts_map.items(), key=lambda kv: (kv[1]["cart"][0], kv[1]["cart"][1]))


def get_initial_state(inp):
    this_map = list(map(lambda i: list(map(lambda i: " ", range(len(inp[0][:-1])))), range(len(inp))))
    carts_map = {}
    cart_id = 0
    carts_order = []
    for x, line in enumerate(inp):
        for y, car in enumerate(line[:-1]):
            if car != " ":
                this_map[x][y] = Milestone(car)
            if car in carts_mapping:
                carts_map[cart_id] = {
                    "cart": np.hstack([np.array([x, y]), carts_mapping[car]]),
                    "status": 0
                }
                carts_order.append(cart_id)
                cart_id += 1
    return this_map, carts_map, carts_order


def run_one_step(this_map, carts_map, carts_order):
    sorted = sort_carts(carts_map)
    for cart_id, cart in sorted:
        milestone = this_map[cart["cart"][0]][cart["cart"][1]]
        if milestone.string == "+":
            action = intersections[np.mod(cart["status"], 3)]
            carts_map[cart_id]["status"] += 1
        else:
            action = milestone.action
        carts_map[cart_id]["cart"] = cart["cart"].dot(action).astype(int)
        collision, carts = check_collisions(cart_id, carts_map)
        if collision:
            return this_map, carts_map, carts_order, True, carts
    return this_map, carts_map, carts_order, False, None


def run_one_step_2(this_map, carts_map, carts_order):
    sorted = sort_carts(carts_map)
    deads = []
    for cart_id, cart in sorted:
        if cart_id in deads:
            continue
        milestone = this_map[cart["cart"][0]][cart["cart"][1]]
        if milestone.string == "+":
            action = intersections[np.mod(cart["status"], 3)]
            carts_map[cart_id]["status"] += 1
        else:
            action = milestone.action
        carts_map[cart_id]["cart"] = cart["cart"].dot(action).astype(int)
        collision, carts = check_collisions(cart_id, carts_map)
        if collision:
            deads += [cart_id, carts[1]]
    carts_map = dict([(cart_id, cart) for cart_id, cart in sorted if cart_id not in deads])

    return this_map, carts_map, carts_order


def clear():
    os.system('clear')


class AOCDay13(AOCDay):

    def __init__(self):
        self.day = 13
        self.split_lines = True

    def display(self, this_map, carts_map):
        clean_sheet = [[" "] * len(this_map[0])] * len(this_map)
        for cart_id, cart in sort_carts(carts_map):
            cart_str = inv_carts_mapping["".join(map(str, cart["cart"][2:]))]
            clean_sheet[cart["cart"][0]][cart["cart"][1]] = colored(cart_str, colors[np.mod(cart_id, len(colors))])
        print("\n".join(map(lambda line: "".join(line), clean_sheet)))
        time.sleep(1)
        clear()

    def run1(self, inp):
        #clear()
        this_map, carts_map, carts_order = get_initial_state(inp)
        iteration = 0
        while True:
            #self.display(this_map, carts_map)
            this_map, carts_map, carts_order, collision, carts = run_one_step(this_map, carts_map, carts_order)
            iteration += 1
            if collision:
                break
        cart_id_1, cart_id_2 = carts
        print("Collision after %d iterations! Cart %d and %d crashed at point (%d, %d)" % (
            iteration,
            cart_id_1,
            cart_id_2,
            carts_map[cart_id_1]["cart"][1],
            carts_map[cart_id_1]["cart"][0]
        )
              )
        return "%s,%s" % (carts_map[cart_id_1]["cart"][1], carts_map[cart_id_1]["cart"][0])

    def run2(self, inp):
        this_map, carts_map, carts_order = get_initial_state(inp)
        iteration = 0
        while True:
            this_map, carts_map, carts_order = run_one_step_2(this_map, carts_map, carts_order)
            iteration += 1
            if len(carts_map) == 1:
                break
        cart_x, cart_y = list(carts_map.values())[0]["cart"][:2]
        print("Iteration %d, last car at position %d,%d" % (
            iteration,
            cart_y,
            cart_x
        )
              )
        return "%s,%s" % (cart_y, cart_x)
