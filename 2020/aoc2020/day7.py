import re


class Bag:

    def __init__(self, name):
        self.name = name
        self.leafs = {}
    
    def add(self, n, bag):
        self.leafs[bag] = int(n)

    def get_descendance(self, bags_collection):
        all_descendants = []
        for bag_name in self.leafs.keys():
            all_descendants.append(bag_name)
            all_descendants += bags_collection[bag_name].get_descendance(bags_collection)
        return all_descendants

    def get_total_descendance(self, bags_collection):
        all_descendants = []
        for bag_name, n_bags in self.leafs.items():
            bag_name_descendance = bags_collection[bag_name].get_total_descendance(bags_collection)
            all_descendants += ([bag_name] + bag_name_descendance) * n_bags
        return all_descendants



def _parse(line):
    clean_line = line.strip()
    node_pattern = r'^(\w+ \w+) bags contain'
    leaf_pattern = r' (\d+) (\w+ \w+) bag[s]?[,.]?'
    node = re.findall(re.compile(node_pattern), clean_line)[0]
    leaf_candidates = re.findall(re.compile(leaf_pattern), clean_line)
    return node, leaf_candidates


def run1(input_path):
    inputs = list(map(_parse, open(input_path).readlines()))
    bags = {}
    bags_containing_shiny_gold = []
    for node_bag, leaf_bags in inputs:
        new_bag = Bag(node_bag)
        bags[node_bag] = new_bag
        for n, leaf_bag in leaf_bags:
            new_bag = Bag(leaf_bag)
            bags[node_bag].add(n, leaf_bag)
    for bag_name, bag in bags.items():
        if 'shiny gold' in bag.get_descendance(bags):
            bags_containing_shiny_gold.append(bag_name)
    return len(bags_containing_shiny_gold)



def run2(input_path):
    inputs = list(map(_parse, open(input_path).readlines()))
    bags = {}
    for node_bag, leaf_bags in inputs:
        new_bag = Bag(node_bag)
        bags[node_bag] = new_bag
        for n, leaf_bag in leaf_bags:
            new_bag = Bag(leaf_bag)
            bags[node_bag].add(n, leaf_bag)
    shiny_gold_descendance = bags['shiny gold'].get_total_descendance(bags)
    return len(shiny_gold_descendance)


if __name__ == '__main__':
    path = 'inputs/tests/day7.txt'
    print(run1(path))
    print(run2(path))
    
    path = 'inputs/day7.txt'
    print(run1(path))
    print(run2(path))

    