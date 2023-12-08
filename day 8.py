import re
import math

def part_1(instructions, tree):
    cur = "AAA"
    trav = 0
    counter = 0
    while cur != "ZZZ":
        if instructions[counter] == "R":
            cur = tree[cur][1]
        if instructions[counter] == "L":
            cur = tree[cur][0]
        trav += 1
        counter = (counter + 1) % len(instructions)

    return trav


def part_2(instructions, tree):
    current_match_list = [key for key in tree.keys() if key.endswith('A')]

    dis = 0
    itera = 0
    stopped=(isinstance(element, int) for element in current_match_list)
    print(all(stopped))
    while not all(isinstance(element, int) for element in current_match_list):
        for idx in range(len(current_match_list)):
            element = current_match_list[idx]
            if isinstance(element, int): continue
            if element.endswith('Z'):
                current_match_list[idx] = int(dis)
                continue

            if instructions[itera] == "R":
                element = tree[element][1]
            if instructions[itera] == "L":
                element = tree[element][0]

            current_match_list[idx] = element

        dis += 1
        itera = (itera + 1) % len(instructions)
        print(all(stopped))
    print(current_match_list)
    sum = math.lcm(*current_match_list)
    return sum


with open("input.txt") as data:
    lines = data.readlines()

    instructions = lines[0][0:-1]
    tree_lines = lines[2:]

    tree = {}
    #i had a worst way to do this byt i found this and it was nice so i stole it. not my code
    pattern = re.compile(r'(\w+)\s*=\s*\((\w+),\s*(\w+)\)')
    for entry in tree_lines:
        match = pattern.match(entry)
        print(match.group(1))
        tree[match.group(1)] = (match.group(2), match.group(3))
    print(tree)
    # Algorithm
    #print(part_1(instructions, tree))
    print("p2",part_2(instructions, tree))
