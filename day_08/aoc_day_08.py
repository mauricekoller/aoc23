from math import gcd


def find_lcm(x, y):
    return x * y // gcd(x, y)


def find_lcm_list(numbers):
    lcm_result = numbers[0]
    for i in range(1, len(numbers)):
        lcm_result = find_lcm(lcm_result, numbers[i])
    return lcm_result


def part_one(text):
    moves = {}
    instructions, possible_moves = text.split('\n\n')

    for line in possible_moves.splitlines():
        starting_node, next_nodes = line.split(' = ')
        left, right = next_nodes[1:-1].split(', ')
        moves[starting_node] = [left, right]

    current_node = 'AAA'
    move_counter = 0
    ZZZ_found = False
    while not ZZZ_found:
        for instruction in instructions:
            if instruction == 'L':
                current_node = moves[current_node][0]
            else:
                current_node = moves[current_node][1]
            move_counter += 1
            if current_node == 'ZZZ':
                ZZZ_found = True
                break

    print(f"Sum Part One: {move_counter}")


def part_two_lcm(text):
    moves = {}
    instructions, possible_moves = text.split('\n\n')

    for line in possible_moves.splitlines():
        starting_node, next_nodes = line.split(' = ')
        left, right = next_nodes[1:-1].split(', ')
        moves[starting_node] = [left, right]

    current_nodes = [node for node in moves.keys() if node[-1] == 'A']
    LCM = [0 for _ in range(len(current_nodes))]
    for idx, node in enumerate(current_nodes):
        move_counter = 0
        current_node = node
        xxz = False
        while not xxz:
            for instruction in instructions:
                if instruction == 'L':
                    current_node = moves[current_node][0]
                else:
                    current_node = moves[current_node][1]
                move_counter += 1
                if current_node[-1] == 'Z':
                    xxz = True
                    LCM[idx] = move_counter
                    break

    move_counter = find_lcm_list(LCM)

    print(f"Sum Part Two: {move_counter}")


def part_two(text):
    moves = {}
    instructions, possible_moves = text.split('\n\n')

    for line in possible_moves.splitlines():
        starting_node, next_nodes = line.split(' = ')
        left, right = next_nodes[1:-1].split(', ')
        moves[starting_node] = [left, right]

    current_nodes = [node for node in moves.keys() if node[-1] == 'A']
    move_counter = 0
    only_z = False
    while not only_z:
        for instruction in instructions:
            if instruction == 'L':
                for idx, node in enumerate(current_nodes):
                    current_nodes[idx] = moves[node][0]
            else:
                for idx, node in enumerate(current_nodes):
                    current_nodes[idx] = moves[node][1]
            move_counter += 1
            if all([node[-1] == 'Z' for node in current_nodes]):
                only_z = True
                break

    print(f"Sum Part Two: {move_counter}")


with open("day_08/input.txt", "r") as input:
    text = input.read().rstrip()
    # lines = text.splitlines()
    part_one(text)
    part_two_lcm(text)
